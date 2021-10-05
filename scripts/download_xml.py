import requests
import re
import os
import git

if os.path.exists('../casasource'): os.system('rm -fr ../casasource')
os.system('mkdir ../casasource')

os.system('git branch > branch_name.txt')
with open('branch_name.txt', 'r') as fid:
    branch_name = [ll for ll in fid.readlines() if ll.startswith('*')][0].strip().split('/')[-1].split(' ')[-1].replace(')','')
    
# see if this branch_name exists in the code repo
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casatasks/xml?at=refs/heads/%s"%branch_name).text
tasknames = list(set(re.findall("\w+.xml", xmlstring)))
if len(tasknames) == 0:
    print('Cant find corresponding code repository, defaulting to master')
    branch_name = 'master'

print('Cloning source for %s code branch' % branch_name)

#############################################################
##
## task xml download from bitbucket code repository
##
#############################################################

# grab the index of all the task xml pages
#xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casatasks/xml?at=refs/heads/%s"%branch_name).text
#tasknames = list(set(re.findall("\w+\.xml", xmlstring)))

# loop through each task xml webpage and parse the xml to python dictionaries
#tasklist = []
#for ii, task in enumerate(tasknames):
#    print('processing ' + str(ii) + ' - ' + task)
#    #xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/" + task).text
#    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casatasks/xml/" + task + '?at=refs/heads/%s'%branch_name).text
#    #xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks/" + task + '?raw').text
#
#    with open('../xml/tasks/'+task, 'w') as fid:
#        fid.write(xmlstring + '\n')

#############################################################
##
## tool xml download from bitbucket code repository
##
#############################################################

# grab the index of all the tool xml pages
#xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casatools/xml?at=refs/heads/%s"%branch_name).text
#toolnames = list(set(re.findall("\w+\.xml", xmlstring)))

#for ii, tool in enumerate(toolnames):
#    print('processing ' + str(ii) + ' - ' + tool)
#    #xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s/%s?raw" % (folder, tool)).text
#    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casatools/xml/%s"%tool + '?at=refs/heads/%s'%branch_name).text
#
#    with open('../xml/tools/'+tool, 'w') as fid:
#        fid.write(xmlstring + '\n')

repo = git.Repo.clone_from('https://open-bitbucket.nrao.edu/scm/casa/casa6.git', '../casasource/casa6', branch=branch_name)

print('complete')


