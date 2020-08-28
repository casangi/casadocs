import requests
import re
import os
import numpy as np
import xml.etree.ElementTree as ET

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

os.system('rm -fr tasks')
os.system('mkdir tasks')
for task in tasklist:
    os.system('mkdir tasks/'+task['category'])
    
    # grab the plone description for this task
    rst = ''
    source = 'html/stable/global-task-list/task_' + task['name'] + '.html'  # assume such a thing exists
    os.system('pandoc %s -f html -t rst -o %s --ascii --extract-media=%s' % (source, 'tasks/temp.rst', 'docs/_media'))
    with open('tasks/temp.rst', 'r') as fid:
        rst = fid.read()
        
    # remove preamble and create heading
    # clean up the conversion mess
    if '..rubric' in rst:
        rst = re.sub('.*?\.\. rubric::.*?:name:.*?\n+', 'Description\n', rst, 1, flags=re.DOTALL)
    else:
        rst = re.sub('.*?parent-fieldname-text\n*', 'Description\n', rst, 1, flags=re.DOTALL)
    #rst = re.sub('\n   ', '\n', rst, flags=re.DOTALL)  # de-indent
    rst = re.sub('(\s*).. container:: \S*-box\s*', r'\1.. note:: ', rst, flags=re.DOTALL)  # change alert boxes
    rst = re.sub('\s*.. container::(\s*\S*)*?\n(\s*:name: \S*\n)?', '\n', rst, flags=re.DOTALL)  # remove container sections
    rst = re.sub('(\.\. \|.*?\| image:: )docs/(\S*)', r'\1../../\2', rst, flags=re.DOTALL)  # fix image links
    rst = rst.replace(' ', ' ').replace('\\ ', ' ').replace('↩ ', '')  # weird ascii things
    rst = re.sub('(:math:\s*`[^\n]+) `', r'\1`', rst, flags=re.DOTALL)  # fix math equations with trailing space before `
    rst = re.sub('\s*[\+\-]+\n\s*\| Citation.*?\n\n', '\n\n', rst, flags=re.DOTALL)  # remove citation tables
    rst = re.sub('\n\s+Bibliography\s*\n', '\n\n\n   Bibliography\n', rst, flags=re.DOTALL)  # fix bibliography indent

    # add this task to the __init__.py
    with open('tasks/'+task['category']+'/'+'__init__.py', 'a') as fid:
        fid.write('from .' + task['name'] + ' import *\n')
    
    # write the python stub function
    with open('tasks/'+task['category']+'/'+task['name']+'.py', 'w') as fid:
        fid.write('#\n# stub function definition file for docstring parsing\n#\n\n')
        
        # build the function prototype, start with params that have no default
        proto = [pp for pp in task['params'] if ('mustexist' in task['params'][pp]) and (task['params'][pp]['mustexist']=='true')]
        proto = ', '.join(proto) + ', ' if len(proto) > 0 else ''
        for param in task['params'].keys():
            # must exist params don't have default values
            if ('mustexist' in task['params'][param]) and (task['params'][param]['mustexist'] == 'true'):
                continue
            elif ('value' in task['params'][param]) and (task['params'][param]['value'] is not None):
                if ('string' in task['params'][param]['type'].split(', ')) or ('variant' in task['params'][param]['type']):
                    proto += param + '=\'' + task['params'][param]['value'].strip() + '\', '
                else:
                    proto += param + '=' + task['params'][param]['value'].strip() + ', '
            else:
                proto += param + "='', "
        fid.write('def %s(%s):\n    r"""\n' % (task['name'], proto[:-2]))
        
        # populate function description
        if 'shortdescription' in task.keys():
            fid.write(task['shortdescription']+'\n\n')
        #if 'description' in task.keys():
        #    fid.write('Summary\n   | '+task['description'].strip().replace('\n','\n   | ') + '\n\n')
        
        # populate function parameters
        fid.write('Parameters\n')
        for param in task['params'].keys():
            # skip subparameters for now, they will go in "other parameters" section later
            if ('subparam' in task['params'][param]) and (task['params'][param]['subparam'].lower() == 'true'):
                continue
            pd = task['params'][param]  # param dictionary
            fid.write('   - **%s** (%s)' % (param, pd['type']))
            if ('shortdescription' in pd.keys()) and (pd['shortdescription'] is not None):
                fid.write(' - %s' % pd['shortdescription'])
            fid.write('\n')

        # populate function subparameters
        if len(task['subparams']) > 0:
            fid.write('\nSubparameters')
        for paramstr in task['subparams'].keys():
            spd = task['subparams'][paramstr]  # subparam dictionary
            if len(spd) > 0:
                fid.write('\n   *%s*\n\n' % paramstr)
            # grab each subparam from the main param section and write it out
            for subparam in spd.keys():
                if subparam not in task['params']: continue
                pd = task['params'][subparam]  # param dictionary
                val = spd[subparam] if len(spd[subparam]) > 1 else spd[subparam][0]
                val = '\'\'' if len(val) == 0 else val
                dtype = ', '.join([vv+'='+val if ii==0 else vv for ii,vv in enumerate(pd['type'].split(', '))])
                fid.write('   - **%s** (%s)' % (subparam, dtype))
                if ('shortdescription' in pd.keys()) and (pd['shortdescription'] is not None):
                    fid.write(' - %s' % pd['shortdescription'])
                fid.write('\n')
        
        # marry up the Plone content to the bottom Notes section
        fid.write('\n\n' + rst)
        fid.write('\n    """\n    pass\n')

os.system('rm tasks/temp.rst')