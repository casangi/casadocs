# CASAdocs
Common Astronomy Software Applications Documentation

- view latest master build at: https://casadocs.readthedocs.io/en/latest  [![Documentation Status](https://readthedocs.org/projects/casadocs/badge/?version=latest)](https://casadocs.readthedocs.io/en/latest/?badge=latest)
- view stable release build at: https://casadocs.readthedocs.io/en/stable  [![Documentation Status](https://readthedocs.org/projects/casadocs/badge/?version=stable)](https://casadocs.readthedocs.io/en/stable/?badge=stable)

A new documentation build is triggered for every commit to the repository. 
It can take 5 to 10 minutes to complete.


## Editing Regular Content
Most of the casadocs content is written in markdown format using the Google
Colab web service to edit Jupyter notebooks of text cells.  Jupyter notebook
pages have a link at the top to "Open in Colab" for editing.  Modified pages
can be saved back in to the casadocs repository from the Colab window under ```File -> Save a copy in Github```.

The nbsphinx package is used to convert notebooks to Sphinx/readthedocs format.
There is some special markdown syntax available that may not render in Google 
Colab.  For the complete set of markdown syntax avaiable, go here:
- https://nbsphinx.readthedocs.io/en/0.7.1/markdown-cells.html

## Editing API Content
API content is generally created by combining xml from the CASA source code
repository with ReStructuredText (rst) files held in the casadocs repository.
The xml can only be updated through development branches of the source code,
while the rst files can be edited directly in the Github repository browser
window.

- Task descriptions can be found under ```docs/tasks```
- Tool descriptions can be found under ```docs/tools```
- Shell descriptions can be found under ```docs/api/casashell```

Sphinx RST syntax and examples can be found here:
- https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html

### Updating XML
When the XML is updated in the CASA source code repo, the files need to be synced back 
to the casadocs repo. This is done through a manually triggered Github Action rather 
than automatically to allow for specific updates to different release branches if necessary.

To update the xml file sync from the CASA source code repo, go to the ```Actions``` tab in
Github, select ```Update_XML``` and click ```Run Workflow```

Verify the files have been updated by navigating to the ```xml``` folder in the root of the
Github repo.

### Adding/Removing/Hiding Tasks
Tasks will only appear in the readthedocs site if they have both an xml file in the ```xml```
folder and a matching rst file in the ```docs/tasks``` folder.  A task can be removed or hidden
from readthedocs by deleting or renaming the rst file to something that does not match the
xml file name.

When a new task is added to CASA, the new xml file will be picked up by the Action described 
above. A new ```rst``` file must also be added to ```docs/tasks``` using the same format as
the others (with sections for Description/Examples/Developer).

## Building Documentation Locally
This documentation repository can be edited and built locally by users with access to Python3. First clone the repo, then navigate to the root of the cloned directory in a terminal and use the following commands:

```
$: python3 -m venv docvenv
$: source docvenv/bin/activate
(docvenv) $: pip install --upgrade pip wheel
(docvenv) $: pip install -r requirements.txt
(docvenv) $: cd docs
(docvenv) $: sphinx-build -a -E -b html . ./build
```

## Re-generating Plone content from Scratch
This should not be necessary and is here only for reference on how
to regenerate the original content from Plone.  

Scrapy and Docker must installed ahead of time, then install the 
python prerequisites from the local build instructions.

1. Scrape the latest Plone CASAdocs (creates html folder):
   ```
   $: scrapy crawl sitemap
   $: docker run -p 8050:8050 scrapinghub/splash
   $: scrapy crawl full
   ```

2. Generate content pages (creates markdown folder)
   ```
   $: python scripts/convert_html.py
   ``` 

3. Generate notebook files (creates docs/notebooks folder)
   ```
   $: python scripts/build_notebooks.py
   ```

4. Locally build pages to verify (this will also call scripts/parse_task_xml.py)
   ```
   $: cd docs
   $: sphinx-build -a -E -b html . ./build
   ```



