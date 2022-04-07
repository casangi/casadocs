import xml.etree.ElementTree as ET
import re
import os
import pypandoc

########################################################
# this is meant to be run from the docs folder
# if running manually, cd docs first
########################################################

pypandoc.pandoc_download.download_pandoc(version='2.10.1')

tools = os.listdir('../casasource/casa6/casatools/xml')
# these tools have had their main descriptions updated to rst
rst_tools = ['agentflagger','calanalysis']

# loop through each tool
tooldict = {}
for tool in tools:
    with open('../casasource/casa6/casatools/xml/' + tool, 'r') as fid:
        xmlstring = fid.read()
        xmlstring = re.sub('\<link.*?\>(.+?)\<\/link>', r'\1', xmlstring, flags=re.DOTALL)
        xmlstring = re.sub('\"\"\"', '', xmlstring, flags=re.DOTALL)
        xmlstring = re.sub('&quot;&quot;&quot;', '', xmlstring, flags=re.DOTALL)
        xmlstring = xmlstring.replace('false', 'False').replace('true', 'True')

    xmlroot = ET.fromstring(xmlstring)

    if '}' not in xmlroot.tag:
        print('### skipping ' + tool)
        continue

    nps = xmlroot.tag[:xmlroot.tag.rindex('}') + 1]
    troot = xmlroot.find(nps + 'tool')  # xml root of the task

    # initialize tool dictionary (td)
    td = [(ee.tag.replace(nps, ''), ee.text) for ee in list(troot) if ee.tag not in [nps + 'method', nps + 'code']]
    td = dict([(ee[0], '' if ee[1] is None else ee[1]) for ee in td])
    td['methods'] = {}

    # loop over each method
    for method in troot.findall(nps + 'method'):
        md = dict([(ee.tag.replace(nps, ''), ee.text) for ee in list(method) if ee.tag not in [nps + 'input']])
        md['params'] = {}
        md['returns'] = None
        md['examples'] = None

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
                        pd['value'] = '[' + ', '.join(
                            ['\'' + ee.text + '\'' if ee.text is not None else '\'\'' for ee in
                             list(param.find(nps + 'value'))]) + ']'
                    elif len(list(param.find(nps + 'value'))) > 0:
                        pd['value'] = '[' + ', '.join([ee.text if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))]) + ']'
                    elif ('stringarray' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')) and (not pd['type'].startswith('\'')):
                        pd['value'] = '[\'' + pd['value'] + '\']' if pd['value'] is not None else '\'\'' #''[\'\']'
                    elif ('array' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                        pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\'' #'[\'\']'
                    elif ('vec' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                        pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\'' #'[\'\']'

                    # can't trust any types, wrap as strings
                    if (pd['type'] == 'any') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                        pd['value'] = '\'' + pd['value'] + '\''
                    if (pd['type'] == 'unknown') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                        pd['value'] = '\'' + pd['value'] + '\''
                    if (pd['type'] == 'record') and (pd['value'] is not None) and (not pd['value'].startswith('\'')):
                        pd['value'] = '\'' + pd['value'] + '\''

                # store parameter dictionary under key equal to parameter name
                md['params'][param.attrib['name']] = pd

        # get the return value of this method
        if method.find(nps + 'returns') is not None:
            iroot = method.find(nps + 'returns')
            md['returns'] = iroot.attrib['type'] if 'type' in iroot.attrib else None

        # get anything in the example section for this method
        if method.find(nps + 'example') is not None:
            iroot = method.find(nps + 'example')
            md['examples'] = iroot.text

        td['methods'][method.attrib['name']] = md
    tooldict[troot.attrib['name']] = td

# limit the tools to the ones we want to process
tools_to_exclude = []
if os.path.exists('tools_selection.csv'):
    with open('tools_selection.csv', 'r') as fin:
        tools_selection = fin.readlines()[0].strip().split(',')
    tools_to_exclude = [name for name in tooldict.keys() if name not in tools_selection]

# clean out old data
if os.path.exists('../casatools'):
    if len(tools_to_exclude) == 0:
        os.system('rm -fr ../casatools')
    else:
        files_to_keep = [f"{name}.py" for name in tools_to_exclude]
        for f in os.listdir('../casatools'):
            if f not in files_to_keep:
                os.system(f"rm -rf ../casatools/{f}")
if not os.path.exists('../casatools'):
    os.system('mkdir ../casatools')

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
        if (('string' in pd['type'].split(', ')) or ('variant' in ptype)) and (not pd['value'].startswith('\'')):
            proto = '%s (%s=\'%s\')' % (param, ptype, pd['value'].strip())
        else:
            proto = '%s (%s=%s)' % (param, ptype, pd['value'].strip())
    return proto


# remove weird formatting issues in the xml descriptions
# separate first line from rest for using the dropdown expander
def cleanxml(text, block=False):
    # text = re.sub(r'<.*?>', '', text, flags=re.DOTALL).replace('\\', '').strip()
    # text = text.replace('begin{equation}', '').replace('end{equation}','')
    # text = text.replace('begin{verbatim}', '').replace('end{verbatim}', '')
    # text = text.replace('*', '\\*').replace('`', '\'').replace('|', r'\|')
    # if block:
    #    text = '|   ' + re.sub('\n', '\n|   ', text.strip(), flags=re.DOTALL)
    # else:
    # text = re.sub('\s+', ' ', text.strip(), flags=re.DOTALL)
    text = re.sub('(\n   )   (\+|\|)', r'\1\2', text, flags=re.DOTALL)
    return text.strip()

def tool_rst_exists(name):
    return os.path.exists('tools/tool_' + name + '.rst')

# include tools in the __init__.py
tools_to_init  = [name for name in tooldict.keys()  if tool_rst_exists(name)]
tools_to_init += [name for name in tools_to_exclude if tool_rst_exists(name)]
with open('../casatools/' + '__init__.py', 'a') as fid:
    for name in tools_to_init:
        fid.write('from .' + name + ' import *\n')

toolnames = []
for name in tooldict.keys():
    if name in tools_to_exclude:
        print(f"({name})")
        continue
    print(name)

    # grab rst description page if it exists, otherwise skip this task
    if not tool_rst_exists(name):
        continue
    with open('tools/tool_' + name + '.rst', 'r') as fid:
        rst = fid.read()

    tool = tooldict[name]

    # change image links
    rst = re.sub('(\.\. \|.*?\| image:: )_apimedia/(\S*)\s*?\n', r'\1../../tools/_apimedia/\2\n', rst, flags=re.DOTALL)
    rst = re.sub('(\.\. figure:: )_apimedia/(\S*)\s*?\n', r'\1../../tools/_apimedia/\2\n', rst, flags=re.DOTALL)

    # start output string to write new stub class
    ostr = '#\n# stub class definition file for docstring parsing\n#\n\n'
    ostr += 'class %s:\n    r"""\n' % name

    # populate class description
    if ('shortdescription' in tool.keys()) and (tool['shortdescription'] is not None) and (len(tool['shortdescription'].strip()) > 0):
        ostr += ' '*4 + cleanxml(tool['shortdescription']).replace('\n', '\n' + ' ' * 4) + '\n\n'
    else:
        ostr += ' '*4 + tool + ' class\n\n'

    if ('description' in tool.keys()) and (tool['description'] is not None) and (len(tool['description'].strip()) > 0):
        #desc = pypandoc.convert_text(tool['description'].replace('_', '\_').replace(r'\\_', '\_'), 'rst', format='latex', extra_args=['--wrap=none'])
        try:
            fromformat = 'latex' if name not in rst_tools else 'rst'
            desc = pypandoc.convert_text(re.sub('(\s\w*?)\_(\w*?)', r'\1\_\2', tool['description'], flags=re.DOTALL), 'rst', format=fromformat, extra_args=['--wrap=none'])
        except:
            desc = tool['description']
        #desc = re.sub('(\s\\\\w*?)\_(\w*?)', r'\1_\2', tool['description'].replace('_', '\_'), flags=re.DOTALL)
        #desc = pypandoc.convert_text(desc, 'rst', format='latex', extra_args=['--wrap=none'])
        ostr += ' ' * 4 + desc.replace('\n', '\n' + ' ' * 4) + '\n\n'
    ostr += ' ' * 4 + '"""\n\n'

    # build the class definition
    for method in tool['methods'].keys():
        toolnames += [name + '.' + method]
        # build method stub, start with params that have no default
        tm = tool['methods'][method]

        # create a method description
        desc = ' ' * 8 + method + ' method\n\n'
        if ('description' in tm.keys()) and (tm['description'] is not None) and (len(tm['description'].strip()) > 0):
            try:
                # desc = ' ' * 8 + pypandoc.convert_text(tm['description'].replace('_', '\_').replace(r'\\_', '\_'), 'rst', format='latex', extra_args=['--wrap=none']).replace('\n', '\n' + ' ' * 8) + '\n\n'
                desc = ' ' * 8 + pypandoc.convert_text(re.sub('(\s\w*?)\_(\w*?)', r'\1\_\2', tm['description'], flags=re.DOTALL).replace('\\\\','\\'), 'rst', format='latex', extra_args=['--wrap=none']).replace('\n', '\n' + ' ' * 8) + '\n\n'
            except:
                # desc = ' ' * 8 + pypandoc.convert_text(tm['description'], 'rst', format='markdown', extra_args=['--wrap=none']).replace('\n', '\n' + ' ' * 8) + '\n\n'
                desc = ' ' * 8 + tm['description'].replace('\n', '\n' + ' ' * 8) + '\n\n'
        elif ('shortdescription' in tm.keys()) and (tm['shortdescription'] is not None) and (len(tm['shortdescription'].strip()) > 0):
            desc = ' ' * 8 + cleanxml(tm['shortdescription']).replace('\n', '\n' + ' ' * 8) + '\n\n' + ' ' * 8 + '\n\n'

        # some methods have no parameters
        if ('params' not in tm.keys()) or (len(tm['params']) == 0):
            ostr += '    def %s(self):\n        r"""\n%s\n\n        """\n\n        pass\n\n' % (method, desc)
            continue

        proto = [pp for pp in tm['params'] if ('mustexist' in tm['params'][pp]) and (tm['params'][pp]['mustexist'] == 'true')]
        proto = ', '.join(proto) + ', ' if len(proto) > 0 else ''
        for param in tm['params'].keys():
            # must exist params don't have default values
            if ('mustexist' not in tm['params'][param]) or (tm['params'][param]['mustexist'] == 'false'):
                proto += '%s%s, ' % (param, ParamSpec(method, param)[ParamSpec(method, param).rindex('='):-1])

        # populate method protoype and description
        ostr += '    def %s(self, %s):\n        r"""\n%s\n\n' % (method, proto[:-2], desc)

        # populate method parameters
        ostr += ' ' * 8 + '.. rubric:: Parameters\n\n'
        for param in tm['params'].keys():
            ostr += ' ' * 8 + '- ``%s``' % ParamSpec(method, param)
            if ('description' in tm['params'][param].keys()) and (tm['params'][param]['description'] is not None) and (
                    len(tm['params'][param]['description'].strip()) > 0):
                ostr += ' - %s' % cleanxml(tm['params'][param]['description']).replace('\n', '  ')
            elif ('shortdescription' in tm['params'][param].keys()) and (
                    tm['params'][param]['shortdescription'] is not None):
                if len(tm['params'][param]['shortdescription'].strip()) > 0:
                    ostr += ' - %s' % cleanxml(tm['params'][param]['shortdescription']).replace('\n', '  ')
            ostr += '\n'

        # populate method Returns
        if (tm['returns'] is not None) and (len(str(tm['returns']).strip()) > 0):
            ostr += '\n\n' + ' '*8 + '.. rubric:: Returns\n\n'
            ostr += ' ' * 8 + '``%s``\n\n' % str(tm['returns'])

        # populate method Examples
        if (tm['examples'] is not None) and (len(str(tm['examples']).strip()) > 0):
            ostr += ' '*8 + '.. rubric:: Examples\n\n'
            ostr += ' '*8 + '::\n\n'
            ostr += ' ' * 11 + tm['examples'].replace('\n', '\n' + ' ' * 11)

        # close docstring stub
        ostr += '\n' + ' ' * 8 + '"""\n\n' + ' ' * 8 + 'pass\n\n\n'

    # marry up the Plone content to the bottom Notes section
    # fid.write('\n\n    """' + rst + '\n\n    """')

    # write the python stub class
    with open('../casatools/' + name + '.py', 'w') as fid:
        fid.write(ostr)
