import requests
import re
import os
import numpy as np

# grab the index of all the task xml pages
xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/").text
tasknames = np.unique(re.findall("\w+.xml", xmlstring))

os.system('mkdir xml')

# loop through each task xml webpage and parse the xml to python dictionaries
tasklist = []
for task in tasknames:
    print('processing ' + task)
    xmlstring = requests.get("https://casa.nrao.edu/PloneResource/stable/taskXml/" + task).text
    with open('xml/'+task, 'w') as fid:
        fid.write(xmlstring)
