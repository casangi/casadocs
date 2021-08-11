import xml.etree.ElementTree as ET
import re
import os
import difflib

########################################################
# this is meant to be run from the docs folder
# if running manually, cd docs first
########################################################

# clean out old data
if os.path.exists('../casatasks'): os.system('rm -fr ../casatasks')
os.system('mkdir ../casatasks')


tasknames = os.listdir('../xml/tasks')

# loop through each task xml webpage and parse the xml to python dictionaries
tasklist = []
for ii, task in enumerate(tasknames):
    with open('../xml/tasks/'+task, 'r') as fid:
       xmlstring = fid.read()
       
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
                    pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\'' #'[\'\']'
                elif ('vec' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                    pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\'' #'[\'\']'
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

# read in old baseline task specs for comparison change log
with open('api_baseline.txt', 'r') as fid:
    lines = fid.readlines()
    stable_tasks = dict([(line.split('(')[0].split('.')[-1], line.strip().replace('.'.join(line.split('.')[:2])+'.','')) for line in lines[2:] if line.startswith('casatasks')])
    difflog = ''
    dd = difflib.Differ()


# helper function to return a string of type and default value for a given parameter
def ParamSpec(param):
    pd = task['params'][param]
    ptype = '{%s}'%pd['type'] if len(pd['type'].split(', ')) > 1 else pd['type']
    proto = '%s_ (%s=\'\')' % (param, ptype)
    
    # must exist params don't have default values
    if ('mustexist' in pd) and (pd['mustexist'] == 'true'):
        proto = '%s_ (%s)' % (param, ptype)
    elif ('value' in pd) and (pd['value'] is not None):
        if ('string' in pd['type'].split(', ')) or ('variant' in ptype):
            proto = '%s_ (%s=\'%s\')' % (param, ptype, pd['value'].strip())
        else:
            proto = '%s_ (%s=%s)' % (param, ptype, pd['value'].strip())
    
    return proto


tasknames = []
for task in tasklist:
    
    # grab rst description page if it exists, otherwise skip this task
    rst = ''
    if os.path.exists('tasks/task_' + task['name'] + '.rst'):
        tasknames += [task['name']]
        with open('tasks/task_' + task['name'] + '.rst', 'r') as fid:
            rst = fid.read()
    else:
        continue
        
    if not os.path.exists('../casatasks/'+task['category']):
        os.system('mkdir ../casatasks/'+task['category'])
    
    # change image links
    rst = re.sub('(\.\. \|.*?\| image:: )_apimedia/(\S*)\s*?\n', r'\1../../tasks/_apimedia/\2\n', rst, flags=re.DOTALL)
    rst = re.sub('(\.\. figure:: )_apimedia/(\S*)\s*?\n', r'\1../../tasks/_apimedia/\2\n', rst, flags=re.DOTALL)
    
    # add this task to the __init__.py
    with open('../casatasks/'+task['category']+'/'+'__init__.py', 'a') as fid:
        fid.write('from .' + task['name'] + ' import *\n')
    
    # write the python stub function
    with open('../casatasks/'+task['category']+'/'+task['name']+'.py', 'w') as fid:
        fid.write('#\n# stub function definition file for docstring parsing\n#\n\n')
        
        # build the function prototype, start with params that have no default
        proto = [pp for pp in task['params'] if ('mustexist' in task['params'][pp]) and (task['params'][pp]['mustexist']=='true')]
        proto = ', '.join(proto) + ', ' if len(proto) > 0 else ''
        for param in task['params'].keys():
            # must exist params don't have default values
            if ('mustexist' not in task['params'][param]) or (task['params'][param]['mustexist'] == 'false'):
                proto += '%s%s, ' % (param, ParamSpec(param)[ParamSpec(param).rindex('='):-1])
        proto = '%s(%s)' % (task['name'], proto[:-2])
        fid.write('def ' + proto + ':\n    r"""\n')
        
        # populate function description
        if 'shortdescription' in task.keys():
            fid.write(task['shortdescription']+'\n\n')
        elif 'description' in task.keys():
            fid.write(re.sub('\s+', ' ', task['description'].strip(), flags=re.DOTALL) + '\n\n')
        else:
            fid.write(' \n\n')

        # populate a horizontal toc nav bar
        fid.write('[' + '] ['.join(['`%s`_' % section for section in ['Description', 'Examples', 'Development', 'Details']]) + ']\n\n')

        # populate function parameters
        fid.write('\nParameters\n')
        for param in task['params'].keys():
            # skip subparameters for now, they are handled below for each regular parameter
            if ('subparam' in task['params'][param]) and (task['params'][param]['subparam'].lower() == 'true'):
                continue
            
            fid.write('   - %s' % ParamSpec(param))
            if ('shortdescription' in task['params'][param].keys()) and (task['params'][param]['shortdescription'] is not None):
                if len(task['params'][param]['shortdescription'].strip()) > 0:
                    fid.write(' - %s' % task['params'][param]['shortdescription'])
            fid.write('\n')
            
            # populate function subparameters (if any)
            subparmkeys = [ee for ee in task['subparams'].keys() if ee.startswith(param + ' =') or ee.startswith(param + ' !=')]
            for paramstr in subparmkeys:
                if len(task['subparams'][paramstr]) > 0:
                    fid.write('\n      .. raw:: html\n\n         <details><summary><i> %s </i></summary>\n\n' % paramstr)
                # grab each subparam from the main param section and write it out
                for subparam in task['subparams'][paramstr].keys():
                    if subparam not in task['params']: continue
                    fid.write('      - %s' % ParamSpec(subparam))
                    if ('shortdescription' in task['params'][subparam].keys()) and (task['params'][subparam]['shortdescription'] is not None):
                        if len(task['params'][subparam]['shortdescription'].strip()) > 0:
                            fid.write(' - %s' % task['params'][subparam]['shortdescription'])
                    fid.write('\n')
                if len(task['subparams'][paramstr]) > 0:
                    fid.write('\n      .. raw:: html\n\n         </details>\n')

        # marry up the Plone content to the bottom Notes section
        fid.write('\n\n' + rst + '\n\n')
        
        # add long descriptions of each parameter as footnotes at the bottom
        fid.write('.. _Details:\n\n')
        fid.write('\nParameter Details\n   Detailed descriptions of each function parameter\n\n')
        for param in task['params'].keys():
            if ('description' in task['params'][param].keys()) and (task['params'][param]['description'] is not None):
                fid.write('.. _%s:\n\n' % param)
                fid.write('| ``%s`` - ' % ParamSpec(param).replace('_ ', ' '))
                fid.write('%s\n\n' % re.sub('\n+', '\n|    ', task['params'][param]['description'].strip(), flags=re.DOTALL))

        # close docstring stub
        fid.write('\n    """\n    pass\n')

        # populate changelog by diffing this task to the last release
        if task['name'] not in stable_tasks:
            difflog += '   <li><p><b>' + task['name'] + '</b> - New Task</p></li>\n\n'
        elif not (stable_tasks[task['name']] == proto.replace('\n','')):
            stable_params = re.sub('.+?\((.*?)\)', r'\1', stable_tasks[task['name']], flags=re.DOTALL).split(', ')
            new_params = re.sub('.+?\((.*?)\)', r'\1', proto.replace('\n',''), flags=re.DOTALL).split(', ')
            diff_params = ['<b><del>'+pp.replace('- ','')+'</del></b>' if pp.startswith('- ') else pp.strip() for pp in dd.compare(stable_params, new_params)]
            diff_params = ['<b><ins>' + pp.replace('+ ', '')+'</ins></b>' if pp.startswith('+ ') else pp for pp in diff_params]
            difflog += '   <li><p><b>'+task['name']+'</b>' + '(<i>' + ', '.join(diff_params) + '</i>)</p></li>\n\n'

# look for deleted tasks
for stable_task in stable_tasks:
    if stable_task not in tasknames:
        difflog += '   <li><p><b>' + stable_task + '</b> - Deleted Task</p></li>\n\n'

# write out log of task API diffs
with open('changelog.rst', 'a') as fid:
    fid.write('\n\nAPI Changes\n+++++++++++\n\n.. rubric:: casatasks\n\n')
    fid.write('.. raw:: html\n\n   <ul>\n' + difflog + '   </ul>\n\n|\n')

