import xml.etree.ElementTree as ET
import re
import os
import importlib.util

########################################################
# this is meant to be run from the docs folder
# if running manually, cd docs first
########################################################


################################################################
# Parse the XML of a CASA task and produce a task description dict
def parse_xml(xmlstring):
    xmlroot = ET.fromstring(xmlstring)

    if '}' not in xmlroot.tag:
        print('### skipping ' + task)
        return None

    nps = xmlroot.tag[:xmlroot.tag.rindex('}') + 1]
    troot = xmlroot.find(nps + 'task')  # xml root of the task

    # initialize task dictionary (td)
    td = {'name': troot.attrib['name'], 'category': troot.attrib['category'].split(',')[0].split('/')[0].split(' ')[0]}
    td.update(dict([(ee.tag.replace(nps, ''), ee.text) for ee in list(troot) if ee.tag not in [nps + 'params']]))

    # fix bad category
    if td['category'] == 'import':
        td['category'] = 'data'

    # parameters
    if troot.find(nps + 'input') is not None:
        iroot = troot.find(nps + 'input')
        td['params'] = {}
        td['subparams'] = {}

        for param in iroot.findall(nps + 'param'):
            pd = param.attrib
            pd['shortdescription'] = '' if param.find(nps + 'shortdescription') is None else param.find(
                nps + 'shortdescription').text
            pd['description'] = '' if param.find(nps + 'description') is None else param.find(nps + 'description').text

            # overwrite param type with <type> tags if present
            casa6_type_tags = param.findall(nps + 'type')

            if casa6_type_tags:
                pd['type'] = ', '.join(type_tag.text.replace('path', 'string') for type_tag in casa6_type_tags)
                # these 2 elif are for pre-casa6 xml (limittypes or type attribute)
            elif (param.find(nps + 'any') is not None) and ('limittypes' in param.find(nps + 'any').attrib):
                pd['type'] = ', '.join(param.find(nps + 'any').attrib['limittypes'].split(' '))
            elif (param.find(nps + 'any') is not None) and ('type' in param.find(nps + 'any').attrib):
                pd['type'] = ', '.join(param.find(nps + 'any').attrib['type'].split(' '))

            # overwrite param type with value type if it is still 'any', also store value itself as default
            if param.find(nps + 'value') is not None:
                if ('type' in param.find(nps + 'value').attrib) and (pd['type'] == 'any'):
                    pd['type'] = param.find(nps + 'value').attrib['type']
                pd['value'] = param.find(nps + 'value').text
                if (len(list(param.find(nps + 'value'))) > 0) and ('string' in pd['type']):
                    pd['value'] = '[' + ', '.join(['\'' + ee.text + '\'' if ee.text is not None else '\'\'' for ee in
                                                   list(param.find(nps + 'value'))]) + ']'
                elif len(list(param.find(nps + 'value'))) > 0:
                    pd['value'] = '[' + ', '.join(
                        [ee.text if ee.text is not None else '\'\'' for ee in list(param.find(nps + 'value'))]) + ']'
                elif ('array' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                    pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\''  # '[\'\']'
                elif ('vec' in pd['type'].split(',')[0].lower()) and (not pd['type'].startswith('[')):
                    pd['value'] = '[' + pd['value'] + ']' if pd['value'] is not None else '\'\''  # '[\'\']'
            # store parameter dictionary under key equal to parameter name
            td['params'][param.attrib['name']] = pd

        # subparameter constraints
        if iroot.find(nps + 'constraints') is not None:
            for parent in list(iroot.find(nps + 'constraints')):
                param = parent.attrib['param']
                for condition in list(parent):  # equals, notequals
                    condstr = condition.tag.replace(nps, '').replace('notequals', '!=').replace('equals', '=')
                    paramstr = "%s %s %s" % (
                        param, condstr, condition.attrib['value'] if len(condition.attrib['value']) > 0 else '\'\'')
                    cd = {}  # condition dictionary
                    for sub in list(condition):
                        if sub.tag.replace(nps, '') == 'description': continue
                        cd[sub.attrib['param']] = ['' if ee.text is None else ee.text for ee in
                                                   sub.findall(nps + 'value')]
                    td['subparams'][paramstr] = cd

    return td
################################################################


################################################################
# loop through each task xml webpage and parse the xml to python dictionaries
tasklist, almalist, plotmslist, viewerlist, lithlist = [], [], [], [], []

if os.path.exists('../casatasks'): os.system('rm -fr ../casatasks')
os.system('mkdir ../casatasks')
for task in os.listdir('../casasource/casa6/casatasks/xml'):
    with open('../casasource/casa6/casatasks/xml/' + task, 'r') as fid:
        xmlstring = fid.read()
    td = parse_xml(xmlstring)
    if td is not None: tasklist += [td]

if os.path.exists('../almatasks'): os.system('rm -fr ../almatasks')
os.system('mkdir ../almatasks')
for task in os.listdir('../casasource/almatasks'):
    with open('../casasource/almatasks/' + task, 'r') as fid:
        xmlstring = fid.read()
    td = parse_xml(xmlstring)
    if td is not None: almalist += [td]

if os.path.exists('../almatasks'): os.system('rm -fr ../casaplotms')
os.system('mkdir ../casaplotms')
for task in os.listdir('../casasource/casaplotms'):
    with open('../casasource/casaplotms/' + task, 'r') as fid:
        xmlstring = fid.read()
    td = parse_xml(xmlstring)
    if td is not None: plotmslist += [td]

if os.path.exists('../casaviewer'): os.system('rm -fr ../casaviewer')
os.system('mkdir ../casaviewer')
for task in os.listdir('../casasource/casaviewer'):
    with open('../casasource/casaviewer/' + task, 'r') as fid:
        xmlstring = fid.read()
    td = parse_xml(xmlstring)
    if td is not None: viewerlist += [td]

# casa5 source tree removed by CAS-14179
# msuvbin is under casa6/casatasks and no longer a special case
if os.path.exists('../casalith'): os.system('rm -fr ../casalith')
os.system('mkdir ../casalith')
# casatablebrowser has its own wheel for which the casalith repository has a task wrapper:
# casalith/build-casalith/src/module/private/task_browsetable.py
os.system("cp -r ../casasource/casatablebrowser/src/casatablebrowser/ casalith")
os.system("cp casalith/__casatablebrowser.py casalith/browsetable.py")
spec = importlib.util.spec_from_file_location("browsetable","../casasource/casatablebrowser/src/casatablebrowser/__casatablebrowser.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
td = {"name": "browsetable", "params": {}, "category": "visualization", "shortdescription": module.__doc__, "description": module.__doc__}
if td is not None: viewerlist += [td]


####################################################################
# now we have all the tasks in an array of dictionaries
# for each one, create a python function stub,
# write the parameters to docstring format
# and marry up the Plone description page to the bottom


########################################################
# helper function to return a string of type and default value for a given parameter
def ParamSpec(param):
    pd = task['params'][param]
    ptype = '{%s}' % pd['type'] if len(pd['type'].split(', ')) > 1 else pd['type']
    proto = '%s_ (%s=\'\')' % (param, ptype)

    # must exist params don't have default values
    if ('mustexist' in pd) and (pd['mustexist'] == 'true'):
        proto = '%s_ (%s)' % (param, ptype)
    elif ('value' in pd) and (pd['value'] is not None):
        if (('string' in pd['type'].split(', ')) or ('variant' in ptype)) and (not pd['value'].startswith('\'')):
            proto = '%s_ (%s=\'%s\')' % (param, ptype, pd['value'].strip())
        else:
            proto = '%s_ (%s=%s)' % (param, ptype, pd['value'].strip())

    return proto


########################################################
def render_rst(component, category, text, task):
    if not os.path.exists('../'+component+'/' + category):
        os.system('mkdir ../'+component+'/' + category)

    # change image links
    text = re.sub(r'(\.\. \|.*?\| image:: )_apimedia/(\S*)\s*?\n', r'\1../../tasks/_apimedia/\2\n', text, flags=re.DOTALL)
    text = re.sub(r'(\.\. figure:: )_apimedia/(\S*)\s*?\n', r'\1../../tasks/_apimedia/\2\n', text, flags=re.DOTALL)

    # add this task to the __init__.py
    with open('../'+component+'/' + category + '__init__.py', 'a') as fid:
        fid.write('from .' + task['name'] + ' import *\n')

    # write the python stub function
    with open('../'+component+'/' + category + task['name'] + '.py', 'w') as fid:
        fid.write('#\n# stub function definition file for docstring parsing\n#\n\n')

        # build the function prototype, start with params that have no default
        proto = [pp for pp in task['params'] if ('mustexist' in task['params'][pp]) and (task['params'][pp]['mustexist'] == 'true')]
        proto = (', '.join(proto) + ', ') if len(proto) > 0 else ''
        for param in task['params'].keys():
            # must exist params don't have default values
            if ('mustexist' not in task['params'][param]) or (task['params'][param]['mustexist'] == 'false'):
                proto += '%s%s, ' % (param, ParamSpec(param)[ParamSpec(param).rindex('='):-1])
        proto = '%s(%s)' % (task['name'], proto[:-2])
        fid.write('def ' + proto + ':\n    r"""\n')

        # populate function description
        if 'shortdescription' in task.keys():
            fid.write(task['shortdescription'] + '\n\n')
        elif 'description' in task.keys():
            fid.write(re.sub(r'\s+', ' ', task['description'].strip(), flags=re.DOTALL) + '\n\n')
        else:
            fid.write(' \n\n')

        # populate a horizontal toc nav bar
        if len(text) > 0:  fid.write('[' + '] ['.join(['`%s`_' % section for section in ['Description', 'Examples', 'Development', 'Details']]) + ']\n\n')

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
        fid.write('\n\n' + text + '\n\n')

        # Add long descriptions of each parameter as footnotes at the bottom. For example:
        # .. _paramname:
        # 
        # | ``paramname (paramtype=defaultvalue)`` - description line 1
        # |    description line 2...
        fid.write('.. _Details:\n\n')
        fid.write('\nParameter Details\n   Detailed descriptions of each function parameter\n\n')
        for pname,pval in task['params'].items():
            if ('description' in pval.keys()) and (pval['description'] is not None):
                fid.write('.. _%s:\n\n' % pname)
                fid.write('| ``%s`` - ' % ParamSpec(pname).replace('_ ', ' '))
                fid.write('%s\n\n' % re.sub('\n+', '\n|    ', pval['description'].strip(), flags=re.DOTALL))

        # close docstring stub
        fid.write('\n    """\n    pass\n')

    return


##################################################################################

# render casatasks, almatasks, casaplotms, and casaviewer
for mname, mlist in [('casatasks', tasklist), ('almatasks', almalist), ('casaplotms', plotmslist), ('casaviewer', viewerlist)]:
    tasknames = []
    for task in mlist:
        # grab rst description page if it exists, otherwise skip this task
        rst = ''
        if os.path.exists('tasks/task_' + task['name'] + '.rst'):
            tasknames += [task['name']]
            with open('tasks/task_' + task['name'] + '.rst', 'r') as fid:
                rst = fid.read()
        else:
            continue

        category = task['category']+'/' if mname == 'casatasks' else ''
        render_rst(mname, category, rst, task)



##############################
# render casalith
tasknames = []
for task in lithlist:
    rst = ''
    if os.path.exists('tasks/task_' + task['name'] + '.rst'):
        tasknames += [task['name']]
        with open('tasks/task_' + task['name'] + '.rst', 'r') as fid:
            rst = fid.read()
    else:
        continue
    render_rst('casalith', '', rst, task)
