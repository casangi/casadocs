import xml.etree.ElementTree as ET
import requests
import re
import os
import numpy as np

# grab the index of all the task xml pages
xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/").text
tasknames = np.unique(re.findall("\w+.xml", xmlstring))

# loop through each task xml webpage and parse the xml to python dictionaries
tasklist = []
for task in tasknames:
    print('processing ' + task)
    xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/" + task).text
    xmlroot = ET.fromstring(xmlstring)
    
    if '}' not in xmlroot.tag:
        print('### skipping ' + task)
        continue
    
    nps = xmlroot.tag[:xmlroot.tag.rindex('}')+1]
    troot = xmlroot.find(nps+'task')  # xml root of the task
    
    # initialize task dictionary (td)
    td = {'name': troot.attrib['name'], 'category': troot.attrib['category'].split(',')[0].split('/')[0].split(' ')[0]}
    td.update(dict([(ee.tag.replace(nps, ''), ee.text) for ee in list(troot) if ee.tag not in [nps+'params']]))
    
    # fix bad category
    if td['category'] == 'import':
        td['category'] = 'data'
    
    # parameters
    if troot.find(nps+'input') is not None:
        iroot = troot.find(nps+'input')
        td['params'] = {}
        td['subparams'] = {}
        
        for param in iroot.findall(nps + 'param'):
            pd = param.attrib
            pd['shortdescription'] = '' if param.find(nps+'shortdescription') is None else param.find(nps+'shortdescription').text
            pd['description'] = '' if param.find(nps+'description') is None else param.find(nps+'description').text
            
            # overwrite param type with limittype if present
            if (param.find(nps+'any') is not None) and ('limittypes' in param.find(nps+'any').attrib):
                pd['type'] = ', '.join(param.find(nps+'any').attrib['limittypes'].split(' '))
            elif (param.find(nps + 'any') is not None) and ('type' in param.find(nps + 'any').attrib):
                pd['type'] = ', '.join(param.find(nps + 'any').attrib['type'].split(' '))

            # overwrite param type with value type if it is still 'any', also store value itself as default
            if param.find(nps + 'value') is not None:
                if ('type' in param.find(nps+'value').attrib) and (pd['type'] == 'any'):
                    pd['type'] = param.find(nps+'value').attrib['type']
                pd['value'] = param.find(nps + 'value').text
                if (len(list(param.find(nps + 'value'))) > 0) and ('string' in pd['type']):
                    pd['value'] = '['+', '.join(['\''+ee.text+'\'' if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))])+']'
                elif len(list(param.find(nps + 'value'))) > 0:
                    pd['value'] = '['+', '.join([ee.text if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))])+']'
                elif ('array' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                    pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '[\'\']'
            # store parameter dictionary under key equal to parameter name
            td['params'][param.attrib['name']] = pd
        
        # subparameter constraints
        if iroot.find(nps + 'constraints') is not None:
            for parent in list(iroot.find(nps + 'constraints')):
                param = parent.attrib['param']
                for condition in list(parent):   # equals, notequals
                    condstr = condition.tag.replace(nps,'').replace('notequals','!=').replace('equals','=')
                    paramstr = "%s %s %s" % (param, condstr, condition.attrib['value'] if len(condition.attrib['value']) > 0 else '\'\'')
                    cd = {}  # condition dictionary
                    for sub in list(condition):
                        if sub.tag.replace(nps,'') == 'description': continue
                        cd[sub.attrib['param']] = ['' if ee.text is None else ee.text for ee in sub.findall(nps+'value')]
                    td['subparams'][paramstr] = cd
                
    tasklist += [td]


####################################################################
# now we have all the tasks in an array of dictionaries
# for each one, create a python function stub,
# write the parameters to docstring format
# and marry up the Plone description page to the bottom

# helper function to return a string of type and default value for a given parameter
def ParamSpec(param):
    pd = task['params'][param]
    ptype = '{%s}'%pd['type'] if len(pd['type'].split(', ')) > 1 else pd['type']
    proto = '**%s** (%s=\'\')' % (param, ptype)
    
    # must exist params don't have default values
    if ('mustexist' in pd) and (pd['mustexist'] == 'true'):
        proto = '**%s** (%s)' % (param, ptype)
    elif ('value' in task['params'][param]) and (task['params'][param]['value'] is not None):
        if ('string' in pd['type'].split(', ')) or ('variant' in ptype):
            proto = '**%s** (%s=\'%s\')' % (param, ptype, pd['value'].strip())
        else:
            proto = '**%s** (%s=%s)' % (param, ptype, pd['value'].strip())
    
    return proto



os.system('rm -fr stubs')
os.system('mkdir stubs')
os.system('cp -r tasks/_apimedia/* docs/_api/media/')
for task in tasklist:
    if not os.path.exists('stubs/'+task['category']):
        os.system('mkdir stubs/'+task['category'])
    
    # grab rst plone description tab if it exists
    rst = ''
    if os.path.exists('tasks/task_' + task['name'] + '.rst'):
        with open('tasks/task_' + task['name'] + '.rst', 'r') as fid:
            rst = fid.read()
    # change image links
    rst = re.sub('(\.\. \|.*?\| image:: )tasks/_apimedia/(\S*)\s*?\n.*:height:.*?\n', r'\1../media/\2', rst, flags=re.DOTALL)
    
    # add this task to the __init__.py
    with open('stubs/'+task['category']+'/'+'__init__.py', 'a') as fid:
        fid.write('from .' + task['name'] + ' import *\n')
    
    # write the python stub function
    with open('stubs/'+task['category']+'/'+task['name']+'.py', 'w') as fid:
        fid.write('#\n# stub function definition file for docstring parsing\n#\n\n')
        
        # build the function prototype, start with params that have no default
        proto = [pp for pp in task['params'] if ('mustexist' in task['params'][pp]) and (task['params'][pp]['mustexist']=='true')]
        proto = ', '.join(proto) + ', ' if len(proto) > 0 else ''
        for param in task['params'].keys():
            # must exist params don't have default values
            if ('mustexist' not in task['params'][param]) or (task['params'][param]['mustexist'] == 'false'):
                proto += '%s%s, ' % (param, ParamSpec(param)[ParamSpec(param).rindex('='):-1])
        fid.write('def %s(%s):\n    r"""\n' % (task['name'], proto[:-2]))
        
        # populate function description
        if 'shortdescription' in task.keys():
            fid.write(task['shortdescription']+'\n\n')
        elif 'description' in task.keys():
            fid.write(re.sub('\s+', ' ', task['description'].strip(), flags=re.DOTALL) + '\n\n')
        else:
            fid.write(' \n\n')
        
        # populate function parameters
        fid.write('Parameters\n')
        for param in task['params'].keys():
            # skip subparameters for now, they will go in "other parameters" section later
            if ('subparam' in task['params'][param]) and (task['params'][param]['subparam'].lower() == 'true'):
                continue
            
            fid.write('   - %s' % ParamSpec(param))
            if ('shortdescription' in task['params'][param].keys()) and (task['params'][param]['shortdescription'] is not None):
                fid.write(' - %s' % task['params'][param]['shortdescription'])
            fid.write('\n')
            
            # populate function subparameters (if any)
            subparmkeys = [ee for ee in task['subparams'].keys() if ee.startswith(param + ' =')]
            for paramstr in subparmkeys:
                if len(task['subparams'][paramstr]) > 0:
                    fid.write('\n      .. raw:: html\n\n         <details><summary><i> %s </i></summary>\n\n' % paramstr)
                # grab each subparam from the main param section and write it out
                for subparam in task['subparams'][paramstr].keys():
                    if subparam not in task['params']: continue
                    fid.write('      - %s' % ParamSpec(subparam))
                    if ('shortdescription' in task['params'][subparam].keys()) and (task['params'][subparam]['shortdescription'] is not None):
                        fid.write(' - %s' % task['params'][subparam]['shortdescription'])
                    fid.write('\n')
                if len(task['subparams'][paramstr]) > 0:
                    fid.write('\n      .. raw:: html\n\n         </details>\n')

        # marry up the Plone content to the bottom Notes section
        fid.write('\n\n' + rst)
        fid.write('\n    """\n    pass\n')