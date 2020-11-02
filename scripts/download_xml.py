import requests
import re
import os

if os.path.exists('xml'): os.system('rm -fr xml')
os.system('mkdir xml')
os.system('mkdir xml/tasks')
os.system('mkdir xml/tools')

#############################################################
##
## task xml download from bitbucket code repository
##
#############################################################

# grab the index of all the task xml pages
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks").text
tasknames = list(set(re.findall("\w+.xml", xmlstring)))

# loop through each task xml webpage and parse the xml to python dictionaries
tasklist = []
for ii, task in enumerate(tasknames):
    print('processing ' + str(ii) + ' - ' + task)
    #xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/" + task).text
    #xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/raw/casa5/gcwrap/tasks/" + task).text
    xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tasks/" + task + '?raw').text

    with open('xml/tasks/'+task, 'w') as fid:
        fid.write(xmlstring + '\n')


#############################################################
##
## tool xml download from bitbucket code repository
##
#############################################################

# grab the index of all the task xml pages
xmlstring = requests.get("https://open-bitbucket.nrao.edu/rest/api/1.0/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools").text
xmldict = eval(xmlstring.replace('true','True').replace('false', 'False'))
foldernames = [tool['path']['name'] for tool in xmldict['children']['values'] if tool['type'] == 'DIRECTORY']

for ii, folder in enumerate(foldernames):
    xmldir = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s?raw" % folder).text
    tools = list(set(re.findall("\w+.xml", xmldir)))
    
    # loop through each tool
    for tool in tools:
        print('processing ' + str(ii) + ' - ' + tool)
        xmlstring = requests.get("https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casa5/gcwrap/tools/%s/%s?raw" % (folder, tool)).text
        
        with open('xml/tools/'+tool, 'w') as fid:
            fid.write(xmlstring + '\n')

print('complete')


