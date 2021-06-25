import xml.etree.ElementTree as ET
import re
import os
import requests


with open('api_baseline.txt', 'r') as fid:
    diffversion = fid.readlines()[0].strip()

xmlstring = requests.get('https://casa.nrao.edu/download/devel/xmldoc/pullrequests.xml').text
xmlroot = ET.fromstring(xmlstring)

difflog = ''
for ticket in list(xmlroot):
    date = ticket.find('updateddate').text
    id = ticket.attrib['id']
    component = ticket.find('components').text
    if component == 'Verification': continue
    note = ticket.find('releasenote').text
    if note is not None: note = note.replace('\n','\n   ')
    difflog += '   <li><p><i>%s</i> <b>%s</b> - %s</p></li>\n\n' % (date, id, note)
    

# write out log of tool API diffs
with open('changelog.rst', 'w') as fid:
    fid.write('Change Log\n==========\n\nSummary of differences from ' + diffversion + '\n\nPull Requests\n+++++++++++++\n\n')
    fid.write('.. raw:: html\n\n   <ul>\n' + difflog + '   </ul>\n\n|\n')