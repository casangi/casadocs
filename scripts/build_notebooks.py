##################################################################
# walks through the markdown folder and builds jupyter notebooks
# into the docs/notebooks folder for sphinx rendering
# also generate the main index.rst file for the documentation set
##################################################################
import os
import re
import nbformat

os.system("rm -fr docs/notebooks")
os.system("mkdir docs/notebooks")
os.system('cp -r markdown/_media docs/notebooks/media')

# copy the top level parents to the destination
for file in os.listdir('markdown'):
    if file.endswith('.md'):
        os.system('cp markdown/%s docs/notebooks/%s' % (file, file))

# generate the index.rst file
with open('markdown/index.rst', 'r') as fid:
    rst = fid.read()

rst = re.sub('Description\n', 'Common Astronomy Software Applications\n======================================\n', rst, flags=re.DOTALL)
rst = rst + '\n.. toctree::\n   :hidden:\n   :maxdepth: 3\n\n'

with open('docs/index.rst', 'w') as fid:
    fid.write(rst)


# grab the original list of all pages in casadocs
# this lets us preserve the ordering of pages
with open('scraper/_sitemap.txt') as fid:
    urls = fid.read().splitlines()
    files = [uu.replace('https://casa.nrao.edu/casadocs-devel/stable', 'markdown') for uu in urls if 'stable' in uu][1:]


# merge all child pages in to the parent directory page
# add parent to index.rst toctree as we go
for file in files:
    source = file + '.md'
    parent = re.sub('(markdown/\S+?)/.*', r'\1', file) + '.md'
    if ('global-task-list' in source) or ('global-tool-list' in source): continue
    if source == parent:
        with open('docs/index.rst', 'a') as fid:
            fid.write('   notebooks/%s\n' % parent.split('/')[-1].split('.')[0])
            if parent.endswith('introduction.md'): fid.write('   api\n')
        continue
        
    parent = parent.replace('markdown','docs/notebooks')

    if not os.path.exists(source):
        print('ERROR: missing ' + source)
        continue
    with open(source, 'r') as fid:
        smd = fid.read()
    with open(parent, 'r') as fid:
        pmd = fid.read()
    
    # indent headings of source by the level below the parent
    smd = re.sub('(\n#+) ', r'\1'+'#'*source.count('/')+' ', smd, flags=re.DOTALL)
    smd = re.sub('(\n#+?)# ', r'\1 ', smd, 1, flags=re.DOTALL)   # de-indent the heading by 1
    
    # max limit of 6 heading levels
    smd = re.sub('\n#######+ ', '\n###### ', smd, flags=re.DOTALL)

    # add horizontal rule to separate source from parent
    smd = '\n\n***\n\n' + smd

    # append source to parent and write parent back to disk
    with open(parent, 'w') as fid:
        fid.write(pmd + smd)


# convert the parent pages to jupyter notebooks
# split sections in to separate cells at appropriate level
for parent in os.listdir('docs/notebooks'):
    parent = 'docs/notebooks/' + parent
    if not parent.endswith('.md'): continue

    with open(parent, 'r') as fid:
        md = fid.read()

    nb = nbformat.v4.new_notebook()
    splits = re.split(r'((?<=\n)#{1,4}\s)', md.strip())
    nb.cells += [nbformat.v4.new_markdown_cell(splits[0])]
    for ii in range(1, len(splits), 2):
       nb.cells += [nbformat.v4.new_markdown_cell('#'+splits[ii]+splits[ii+1])]

    nbformat.write(nb, parent.replace('.md','.ipynb'), nbformat.NO_CONVERT)
    os.system('rm %s' % parent)
