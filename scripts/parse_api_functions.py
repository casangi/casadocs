# parses the docs/api rst files and diffs with previous release
# note that tasks and tools are handled separately in the parse_task_xml and parse_tool_xml scripts
import re
import os
import difflib

with open('api_baseline.txt', 'r') as fid:
    lines = fid.readlines()
    stable_shell = dict([(ll.split('(')[0].split('.')[-1], ll.strip().replace('.'.join(ll.split('.')[:1])+'.','')) for ll in lines[2:] if ll.startswith('casashell')])
    stable_data = dict([(ll.split('(')[0].split('.')[-1], ll.strip().replace('.'.join(ll.split('.')[:1])+'.','')) for ll in lines[2:] if ll.startswith('casadata')])
    stable_lith = dict([(ll.split('(')[0].split('.')[-1], ll.strip().replace('.'.join(ll.split('.')[:1]) + '.', '')) for ll in lines[2:] if ll.startswith('casalith')])
    stable_config = dict([(ll.split('(')[0].split('.')[-1], ll.strip().replace('.'.join(ll.split('.')[:1]) + '.', '')) for ll in lines[2:] if ll.startswith('config')])
    dd = difflib.Differ()


################################################3
# parse the casashell directory for function specs
difflog = '\n.. rubric:: casashell\n\n.. raw:: html\n\n   <ul>\n\n'
shellnames = []
for ff in sorted(os.listdir('api/casashell')):
    if not ff.endswith('.rst'): continue
    with open('api/casashell/'+ff) as fid:
        rst = fid.read()
    proto = re.findall('(\.\. function::|\.\. data::) (.+?)\n', rst, flags=re.DOTALL)[0][1]
    if len(proto) == 0: continue
    shellnames += [proto.split('(')[0]]

    if shellnames[-1] not in stable_shell:
        difflog += '   <li><p><b>' + ff.split('.')[0] + '</b> - New Function</p></li>\n\n'
    elif not (stable_shell[shellnames[-1]] == proto.replace('\n', '')):
        stable_params = re.sub('.+?\((.*?)\)', r'\1', stable_shell[shellnames[-1]], flags=re.DOTALL).split(', ')
        new_params = re.sub('.+?\((.*?)\)', r'\1', proto.replace('\n', ''), flags=re.DOTALL).split(', ')
        diff_params = ['<b><del>' + pp.replace('- ', '') + '</del></b>' if pp.startswith('- ') else pp.strip() for pp in dd.compare(stable_params, new_params)]
        diff_params = ['<b><ins>' + pp.replace('+ ', '') + '</ins></b>' if pp.startswith('+ ') else pp for pp in diff_params]
        difflog += '   <li><p><b>' + shellnames[-1] + '</b>' + '(<i>' + ', '.join(diff_params) + '</i>)</p></li>\n\n'

# look for deleted functions
for ff in stable_shell:
    if ff not in shellnames:
        difflog += '   <li><p><b>' + ff + '</b> - Deleted Function</p></li>\n\n'


################################################3
# parse the casadata rst file for specs
with open('api/casadata.rst') as fid:
    rst = fid.read()
    
difflog += '   </ul>\n\n|\n\n.. rubric:: casadata\n\n.. raw:: html\n\n   <ul>\n\n'
protos = re.findall('\.\. data:: (.+?)\n', rst, flags=re.DOTALL)
for proto in protos:
    fname = proto.split('(')[0]
    if fname not in stable_data:
        difflog += '   <li><p><b>' + fname.split('.')[0] + '</b> - New Function</p></li>\n\n'
    elif not (stable_data[fname] == proto.replace('\n', '')):
        stable_params = re.sub('.+?\((.*?)\)', r'\1', stable_data[fname], flags=re.DOTALL).split(', ')
        new_params = re.sub('.+?\((.*?)\)', r'\1', proto.replace('\n', ''), flags=re.DOTALL).split(', ')
        diff_params = ['<b><del>' + pp.replace('- ', '') + '</del></b>' if pp.startswith('- ') else pp.strip() for pp in dd.compare(stable_params, new_params)]
        diff_params = ['<b><ins>' + pp.replace('+ ', '') + '</ins></b>' if pp.startswith('+ ') else pp for pp in diff_params]
        difflog += '   <li><p><b>' + fname + '</b>' + '(<i>' + ', '.join(diff_params) + '</i>)</p></li>\n\n'
difflog += '   </ul>'

# look for deleted functions
for ff in stable_data:
    if ff not in [pp.split('(')[0] for pp in protos]:
        difflog += '   <li><p><b>' + ff + '</b> - Deleted Function</p></li>\n\n'


################################################3
# parse the casalith rst file for specs
with open('api/casalith.rst') as fid:
    rst = fid.read()

difflog += '   </ul>\n\n|\n\n.. rubric:: casalith\n\n.. raw:: html\n\n   <ul>\n\n'
protos = re.findall('\.\. data:: (.+?)\n', rst, flags=re.DOTALL)
for proto in protos:
    fname = proto.split('(')[0]
    if fname not in stable_lith:
        difflog += '   <li><p><b>' + fname.split('.')[0] + '</b> - New Function</p></li>\n\n'
    elif not (stable_lith[fname] == proto.replace('\n', '')):
        stable_params = re.sub('.+?\((.*?)\)', r'\1', stable_lith[fname], flags=re.DOTALL).split(', ')
        new_params = re.sub('.+?\((.*?)\)', r'\1', proto.replace('\n', ''), flags=re.DOTALL).split(', ')
        diff_params = ['<b><del>' + pp.replace('- ', '') + '</del></b>' if pp.startswith('- ') else pp.strip() for pp in dd.compare(stable_params, new_params)]
        diff_params = ['<b><ins>' + pp.replace('+ ', '') + '</ins></b>' if pp.startswith('+ ') else pp for pp in diff_params]
        difflog += '   <li><p><b>' + fname + '</b>' + '(<i>' + ', '.join(diff_params) + '</i>)</p></li>\n\n'
difflog += '   </ul>'

# look for deleted functions
for ff in stable_lith:
    if ff not in [pp.split('(')[0] for pp in protos]:
        difflog += '   <li><p><b>' + ff + '</b> - Deleted Function</p></li>\n\n'



################################################3
# parse the configuration rst file for specs
with open('api/configuration.rst') as fid:
    rst = fid.read()

difflog += '   </ul>\n\n|\n\n.. rubric:: configuration\n\n.. raw:: html\n\n   <ul>\n\n'
protos = re.findall('\.\. data:: (.+?)\n', rst, flags=re.DOTALL)
for proto in protos:
    fname = proto.split('(')[0]
    if fname not in stable_config:
        difflog += '   <li><p><b>' + fname.split('.')[0] + '</b> - New Function</p></li>\n\n'
    elif not (stable_config[fname] == proto.replace('\n', '')):
        stable_params = re.sub('.+?\((.*?)\)', r'\1', stable_config[fname], flags=re.DOTALL).split(', ')
        new_params = re.sub('.+?\((.*?)\)', r'\1', proto.replace('\n', ''), flags=re.DOTALL).split(', ')
        diff_params = ['<b><del>' + pp.replace('- ', '') + '</del></b>' if pp.startswith('- ') else pp.strip() for pp in dd.compare(stable_params, new_params)]
        diff_params = ['<b><ins>' + pp.replace('+ ', '') + '</ins></b>' if pp.startswith('+ ') else pp for pp in diff_params]
        difflog += '   <li><p><b>' + fname + '</b>' + '(<i>' + ', '.join(diff_params) + '</i>)</p></li>\n\n'
difflog += '   </ul>'

# look for deleted functions
for ff in stable_config:
    if ff not in [pp.split('(')[0] for pp in protos]:
        difflog += '   <li><p><b>' + ff + '</b> - Deleted Function</p></li>\n\n'



# write out log of task API diffs
with open('changelog.rst', 'a') as fid:
    fid.write(difflog + '\n\n')
