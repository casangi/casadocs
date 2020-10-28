import xml.etree.ElementTree as ET
import requests
import re
import os

########################################################
# this is meant to be run from the docs folder
# if running manually, cd docs first
########################################################

# grab the index of all the task xml pages
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools").text
xmldict = eval(xmlstring.replace('true','True').replace('false', 'False'))
foldernames = [tool['path']['name'] for tool in xmldict['children']['values'] if tool['type'] == 'DIRECTORY']

# loop through each tool directory
tooldict = {}
for ii, folder in enumerate(foldernames):
    xmldir = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s?raw" % folder).text
    tools = list(set(re.findall("\w+.xml", xmldir)))
    
    # loop through each tool
    for tool in tools:
        xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s/%s?raw" % (folder, tool)).text
        xmlroot = ET.fromstring(xmlstring)
        print('processing ' + str(ii) + ' - ' + tool)
    
        if '}' not in xmlroot.tag:
            print('### skipping ' + tool)
            continue
    
        nps = xmlroot.tag[:xmlroot.tag.rindex('}') + 1]
        troot = xmlroot.find(nps + 'tool')  # xml root of the task
        
        # initialize tool dictionary (td)
        td = dict([(ee.tag.replace(nps, ''), ee.text) for ee in list(troot) if ee.tag not in [nps+'method', nps+'code']])
        td['methods'] = {}
    
        # loop over each method
        for method in troot.findall(nps + 'method'):
            md = dict([(ee.tag.replace(nps, ''), ee.text) for ee in list(method) if ee.tag not in [nps+'input']])
            md['params'] = {}
            
            # build parameter dictionary
            if method.find(nps + 'input') is not None:
                iroot = method.find(nps + 'input')
                
                for param in iroot.findall(nps + 'param'):
                    pd = param.attrib
                    pd['shortdescription'] = '' if param.find(nps + 'shortdescription') is None else param.find(nps + 'shortdescription').text
                    pd['description'] = '' if param.find(nps + 'description') is None else param.find(nps + 'description').text
            
                    # overwrite param type with limittype if present
                    if (param.find(nps + 'any') is not None) and ('limittypes' in param.find(nps + 'any').attrib):
                        pd['type'] = ', '.join(param.find(nps + 'any').attrib['limittypes'].split(' '))
                    elif (param.find(nps + 'any') is not None) and ('type' in param.find(nps + 'any').attrib):
                        pd['type'] = ', '.join(param.find(nps + 'any').attrib['type'].split(' '))
            
                    # overwrite param type with value type if it is still 'any', also store value itself as default
                    if param.find(nps + 'value') is not None:
                        if ('type' in param.find(nps + 'value').attrib) and (pd['type'] == 'any'):
                            pd['type'] = param.find(nps + 'value').attrib['type']
                        pd['value'] = param.find(nps + 'value').text
                        if pd['value'] is not None:
                            pd['value'] = pd['value'].strip().replace('true', 'True').replace('false', 'False')
                        if (len(list(param.find(nps + 'value'))) > 0) and ('string' in pd['type']):
                            pd['value'] = '[' + ', '.join(['\'' + ee.text + '\'' if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))]) + ']'
                        elif len(list(param.find(nps + 'value'))) > 0:
                            pd['value'] = '[' + ', '.join([ee.text if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))]) + ']'
                        elif ('stringarray' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')) and (not pd['type'].startswith('\'')):
                            pd['value'] = '[\'' + pd['value'] + '\']' if pd['value'] is not None else '[\'\']'
                        elif ('array' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                            pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '[\'\']'
                        
                        # can't trust any types, wrap as strings
                        if (pd['type'] == 'any') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                            pd['value'] = '\'' + pd['value'] + '\''
                        if (pd['type'] == 'unknown') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                            pd['value'] = '\'' + pd['value'] + '\''
                        if (pd['type'] == 'record') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                            pd['value'] = '\'' + pd['value'] + '\''

                    # store parameter dictionary under key equal to parameter name
                    md['params'][param.attrib['name']] = pd
                    
            td['methods'][method.attrib['name']] = md
        tooldict[troot.attrib['name']] = td


####################################################################
# now we have all the tasks in an array of dictionaries
# for each one, create a python function stub,
# write the parameters to docstring format
# and marry up the Plone description page to the bottom

# helper function to return a string of type and default value for a given parameter
def ParamSpec(method, param):
    pd = tool['methods'][method]['params'][param]
    ptype = '{%s}' % pd['type'] if len(pd['type'].split(', ')) > 1 else pd['type']
    proto = '%s (%s=\'\')' % (param, ptype)
    
    # must exist params don't have default values
    if ('mustexist' in pd) and (pd['mustexist'] == 'true'):
        proto = '%s (%s)' % (param, ptype)
    elif ('value' in pd) and (pd['value'] is not None):
        if ('string' in pd['type'].split(', ')) or ('variant' in ptype):
            proto = '%s (%s=\'%s\')' % (param, ptype, pd['value'].strip())
        else:
            proto = '%s (%s=%s)' % (param, ptype, pd['value'].strip())
    return proto

# remove weird formatting issues in the xml descriptions
# separate first line from rest for using the dropdown expander
def cleanxml(text):
    text = re.sub(r'<.*?>', '', text, flags=re.DOTALL).replace('\\', '').strip()
    #text = re.sub('\n', '\n| ', text, flags=re.DOTALL)
    return text.strip()


# clean out old data
if os.path.exists('../casatools'): os.system('rm -fr ../casatools')
os.system('mkdir ../casatools')

for name in tooldict.keys():
    
    # grab rst description page if it exists, otherwise skip this task
    rst = ''
    if os.path.exists('tools/tool_' + name + '.rst'):
        with open('tools/tool_' + name + '.rst', 'r') as fid:
            rst = fid.read()
    else:
        continue
    
    tool = tooldict[name]
    
    # change image links
    rst = re.sub('(\.\. \|.*?\| image:: )_apimedia/(\S*)\s*?\n', r'\1../../tools/_apimedia/\2\n', rst, flags=re.DOTALL)
    
    # add this tool to the __init__.py
    with open('../casatools/' + '__init__.py', 'a') as fid:
        fid.write('from .' + name + ' import *\n')
    
    # write the python stub class
    with open('../casatools/' + name + '.py', 'w') as fid:
        fid.write('#\n# stub class definition file for docstring parsing\n#\n\n')
        fid.write('class %s:\n    """\n' % name)

        # populate class description
        if ('shortdescription' in tool.keys()) and (tool['shortdescription'] is not None) and (len(tool['shortdescription'].strip()) > 0):
            fid.write(cleanxml(tool['shortdescription']) + '\n\n')
        if ('description' in tool.keys()) and (tool['description'] is not None) and (len(tool['description'].strip()) > 0):
            fid.write(cleanxml(tool['description']) + '\n\n')
        fid.write('    """\n\n')
        
        # build the class definition
        for method in tool['methods'].keys():
            # build method stub, start with params that have no default
            tm = tool['methods'][method]
            
            # create a method description
            desc = ''
            if ('shortdescription' in tm.keys()) and (tm['shortdescription'] is not None):
                desc = cleanxml(tm['shortdescription']) + '\n\n'
            if ('description' in tm.keys()) and (tm['description'] is not None) and (len(tm['description'].strip()) > 0):
                desc = desc + cleanxml(tm['description']) + '\n'
                
            # some methods have no parameters
            if ('params' not in tm.keys()) or (len(tm['params']) == 0):
                fid.write('    def %s(self):\n        """\n%s\n\n        """\n\n        pass\n\n' % (method, desc))
                continue
            
            proto = [pp for pp in tm['params'] if ('mustexist' in tm['params'][pp]) and (tm['params'][pp]['mustexist'] == 'true')]
            proto = ', '.join(proto) + ', ' if len(proto) > 0 else ''
            for param in tm['params'].keys():
                # must exist params don't have default values
                if ('mustexist' not in tm['params'][param]) or (tm['params'][param]['mustexist'] == 'false'):
                    proto += '%s%s, ' % (param, ParamSpec(method, param)[ParamSpec(method, param).rindex('='):-1])
            
            # populate method protoype and description
            fid.write('    def %s(self, %s):\n        """\n%s\n\n' % (method, proto[:-2], desc))
            
            # populate method parameters
            fid.write('.. rubric:: Parameters\n\n')
            for param in tm['params'].keys():
                fid.write('- ``%s``' % ParamSpec(method, param))
                if ('description' in tm['params'][param].keys()) and (tm['params'][param]['description'] is not None) and (len(tm['params'][param]['description'].strip()) > 0):
                    fid.write(' - %s' % cleanxml(tm['params'][param]['description']))
                elif ('shortdescription' in tm['params'][param].keys()) and (tm['params'][param]['shortdescription'] is not None):
                    if len(tm['params'][param]['shortdescription'].strip()) > 0:
                        fid.write(' - %s' % cleanxml(tm['params'][param]['shortdescription']))
                fid.write('\n')
            
            # close docstring stub
            fid.write('\n        """\n\n        pass\n\n\n')
            
        # marry up the Plone content to the bottom Notes section
        #fid.write('\n\n    """' + rst + '\n\n    """')
