import requests
import re
import os

if os.path.exists('../xml'): os.system('rm -fr ../xml')
os.system('mkdir ../xml')
os.system('mkdir ../xml/tasks')
os.system('mkdir ../xml/tools')

os.system('git branch > branch_name.txt')
with open('branch_name.txt', 'r') as fid:
    branch_name = [ll for ll in fid.readlines() if ll.startswith('*')][0].strip().split('/')[-1].split(' ')[-1].replace(')','')

# if this is a release branch, we need to look in the release folder
if len(re.findall('v\d\.', branch_name)) > 0:
    branch_name = 'release/' + branch_name[1:]

# see if this branch_name exists in the code repo
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks?at=refs/heads/%s"%branch_name).text
tasknames = list(set(re.findall("\w+.xml", xmlstring)))
if len(tasknames) == 0:
    print('Cant find corresponding code repository, defaulting to master')
    branch_name = 'master'

print('Downloading xml for %s code branch' % branch_name)

#############################################################
##
## task xml download from bitbucket code repository
##
#############################################################

# grab the index of all the task xml pages
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks?at=refs/heads/%s"%branch_name).text
tasknames = list(set(re.findall("\w+.xml", xmlstring)))

# loop through each task xml webpage and parse the xml to python dictionaries
tasklist = []
for ii, task in enumerate(tasknames):
    print('processing ' + str(ii) + ' - ' + task)
    #xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/" + task).text
    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casa5/gcwrap/tasks/" + task + '?at=refs/heads/%s'%branch_name).text
    #xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks/" + task + '?raw').text

    with open('../xml/tasks/'+task, 'w') as fid:
        fid.write(xmlstring + '\n')


#############################################################
##
## tool xml download from bitbucket code repository
##
#############################################################

# grab the index of all the tool xml pages
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools?at=refs/heads/%s"%branch_name).text
xmldict = eval(xmlstring.replace('true','True').replace('false', 'False'))
foldernames = [tool['path']['name'] for tool in xmldict['children']['values'] if tool['type'] == 'DIRECTORY']

for ii, folder in enumerate(foldernames):
    #xmldir = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s?raw" % folder).text
    xmldir = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casa5/gcwrap/tools/%s"%folder + '?at=refs/heads/%s'%branch_name).text
    tools = list(set(re.findall("\w+.xml", xmldir)))
    
    # loop through each tool
    for tool in tools:
        print('processing ' + str(ii) + ' - ' + tool)
        #xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s/%s?raw" % (folder, tool)).text
        xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casa5/gcwrap/tools/%s/%s"%(folder, tool) + '?at=refs/heads/%s'%branch_name).text
        with open('../xml/tools/'+tool, 'w') as fid:
            fid.write(xmlstring + '\n')

print('complete')


