##########################################################################
# download the xml and/or source code for all the various casa packages
##########################################################################
import requests
import subprocess
import re
import os
import git

os.system('git branch > branch_name.txt')
with open('branch_name.txt', 'r') as fid:
    branch_name = [ll for ll in fid.readlines() if ll.startswith('*')][0].strip().split('/')[-1].split(' ')[-1].replace(')','')

# if this is a release branch, we need to look in the release folder
if len(re.findall(r'v\d\.', branch_name)) > 0:
    branch_name = 'release/' + branch_name[1:]

casadocs_branch_name = branch_name

# see if this branch_name exists in the code repo
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casatasks/xml?at=refs/heads/%s"%branch_name).text
tasknames = list(set(re.findall(r"\w+.xml", xmlstring)))
if len(tasknames) == 0:
    # this could be a tag (like a stable build) instead of a real branch, try to resolve the hash and see
    os.system('git name-rev %s > branch_tag.txt' % branch_name)
    with open('branch_tag.txt', 'r') as fid:
        tag = fid.read()
        if len(tag) > 0:
            branch_name = 'release/' + tag.split('\n')[0].strip().split('/')[-1].split('-')[0][1:]

xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casatasks/xml?at=refs/heads/%s" % branch_name).text
tasknames = list(set(re.findall(r"\w+.xml", xmlstring)))
if len(tasknames) == 0:
    print('Cant find corresponding code repository, defaulting to master')
    branch_name = 'master'

if os.path.exists('../casasource'): os.system('rm -fr ../casasource')
os.system('mkdir ../casasource')

# cloning the repo is a bit faster than retrieving each xml file one at a time
print('Cloning source for %s code branch' % branch_name)
repo = git.Repo.clone_from('https://open-bitbucket.nrao.edu/scm/casa/casa6.git', '../casasource/casa6', branch=branch_name)
# browsetable remains a special case, now without maintained XML data
repo = git.Repo.clone_from("https://open-bitbucket.nrao.edu/scm/casa/casatablebrowser.git", "../casasource/casatablebrowser", branch=branch_name)


##################################################################################
# for casaconfig, using a limited clone with blob:none to avoid large
# sizes due to long-deleted data directory
##################################################################################
if os.path.exists('../casaconfig'): os.system('rm -fr ../casaconfig')
os.system('mkdir ../casaconfig')
# see if this casadocs branch exists for casaconfig, else use master
print("looking for casaconfig branch %s" % casadocs_branch_name)
cmd = 'git ls-remote --heads https://github.com/casangi/casaconfig.git %s | wc -l' % casadocs_branch_name
proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
out = proc.stdout.read()
print("cmd out is %s" % out)
casaconfig_branch_name = casadocs_branch_name if (int(out)==1) else 'master'
print('Limited clone of casaconfig for %s branch' % casaconfig_branch_name)
repo = git.Repo.clone_from('https://github.com/casangi/casaconfig.git', '../casaconfig/casaconfig-%s' % casaconfig_branch_name, filter='blob:none', branch=casaconfig_branch_name)
# rearrange things to where the rest of the the casadocs build expects to find them
os.system('mv ../casaconfig/casaconfig-*/casaconfig/*.py ../casaconfig/.')
os.system('mv ../casaconfig/casaconfig-*/casaconfig/private ../casaconfig/.')
os.system('rm -fr ../casaconfig/casaconfig-*')
# copy file to be used showing the defaults
os.system('cp ../casaconfig/private/config_defaults_static.py .')


##################################################################################
# get xml from other packages (formerly in casatasks) from their proper places
##################################################################################
print('Downloading ALMAtasks...')
os.system('mkdir ../casasource/almatasks')
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/almatasks/browse/xml?at=refs/heads/%s"%branch_name).text
package_branch_name = 'master' if len(set(re.findall(r"\w+\.xml", xmlstring))) == 0 else branch_name
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/almatasks/browse/xml?at=refs/heads/%s"%package_branch_name).text
for name in set(re.findall(r"\w+\.xml", xmlstring)):
    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/almatasks/raw/xml/%s"%name+'?at=refs/heads/%s'%package_branch_name).text
    with open('../casasource/almatasks/'+name, 'w') as fid:
        fid.write(xmlstring + '\n')

print('Downloading CASAplotms...')
os.system('mkdir ../casasource/casaplotms')
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casaplotms/browse/src/xml?at=refs/heads/%s"%branch_name).text
package_branch_name = 'master' if len(set(re.findall(r"\w+\.xml", xmlstring))) == 0 else branch_name
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casaplotms/browse/src/xml?at=refs/heads/%s"%package_branch_name).text
for name in set(re.findall(r"\w+\.xml", xmlstring)):
    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casaplotms/raw/src/xml/%s"%name + '?at=refs/heads/%s'%package_branch_name).text
    with open('../casasource/casaplotms/'+name, 'w') as fid:
        fid.write(xmlstring + '\n')

print('Downloading CASAviewer...')
os.system('mkdir ../casasource/casaviewer')
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casaviewer/browse/src/xml?at=refs/heads/%s"%branch_name).text
package_branch_name = 'master' if len(set(re.findall(r"\w+\.xml", xmlstring))) == 0 else branch_name
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casaviewer/browse/src/xml?at=refs/heads/%s"%package_branch_name).text
for name in set(re.findall(r"\w+\.xml", xmlstring)):
    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casaviewer/raw/src/xml/%s"%name + '?at=refs/heads/%s'%package_branch_name).text
    with open('../casasource/casaviewer/'+name, 'w') as fid:
        fid.write(xmlstring + '\n')
