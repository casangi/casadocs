import os
import re
import nbformat

# toctree pages
header = """
===================================

"""
body = """
.. toctree::
   :hidden:
   :maxdepth: 3

"""

# notebook template
blank_meta = {"colab": {"provenance": [],"collapsed_sections": [], "toc_visible": True, "include_colab_link": True},
                        "kernelspec": {"name": "python3", "display_name": "Python 3"}}

# grab the list of all pages in casadocs
with open('scraper/_sitemap.txt') as fid:
    urls = fid.read().splitlines()
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging']

# each page in casadocs should have already been downloaded by the scrapy spider to an html file
# the local html directory structure should match the casadocs website structure
# we will execute pandoc on each of these files to convert their format
for ii, url in enumerate(urls):
    fpath = ['html'] + url.split("/")[4:]
    source = '/'.join(fpath) + '.html'
    if os.path.exists(source):
        print('converting %s of %s...' % (str(ii), str(len(urls))), end='\r')
        
        fpath = ['docs', '_files'] + url.split("/")[5:]
        for ii in range(1,len(fpath)):
            subdir = '/'.join(fpath[:ii])
            if not os.path.isdir(subdir):
                os.mkdir(subdir)
        dest = '/'.join(fpath) + '.ipynb'
        
        # use pandoc to convert html to markdown
        os.system('pandoc %s -s -f html -t ipynb -o %s --atx-headers --extract-media=%s' % (source, dest, '/'.join(fpath[:-1])))
        #os.system('pandoc %s -f html -t rst -o %s' % (source, dest+'.rst'))
        #os.system('pandoc %s -f rst -t ipynb -o %s' % (dest+'.rst', dest+'.ipynb'))
        
        # now we need to manually fix the notebook to conform to nbsphinx conversion limitations
        nb = nbformat.read(dest, nbformat.NO_CONVERT)
        md = nb.cells[0]['source']
        
        # get rid of extraneous span tags
        md = re.sub('<span(.|\n)*?>','', md)
        md = re.sub('</span>', '', md)
        
        # fix image links to work properly
        md = re.sub('<img src="(.+?)" .+?/>', r'![image](\1)', md)
        md = re.sub('attachment:%s/' % '/'.join(fpath[:-1]), '', md)
        
        # split sections in to separate cells at appropriate level
        splits = re.split('(#+([^#]|\n)+)', md)
        splits = [split for split in splits if split.strip()]
        for ii, split in enumerate(splits):
            if ii == 0:
                nb.cells[0] = nbformat.v4.new_markdown_cell(split)
            else:
                nb.cells += [nbformat.v4.new_markdown_cell('#'+split)]
        
        #nb.cells[0]['source'] = md
        nbformat.write(nb, dest, nbformat.NO_CONVERT)
        
        ## add each file to the toctree of the parent folder
        if len(fpath) > 2:
            # we need to extract the proper title
            with open(source, 'r') as fid:
                lines = fid.read()
            title = re.search('<h1 class="documentFirstHeading">(.+?)</h1>', lines).group(1)
            
            fname = '/'.join(fpath[:-1]) + '.ipynb'
            nb = nbformat.read(fname, nbformat.NO_CONVERT)
            
            # the last cell should be the toctree, if not, create a new cell with one
            if 'nbsphinx-toctree' not in nb.cells[-1]['metadata']:
                toctree = nbformat.from_dict({'cell_type': 'markdown', 'metadata': {"nbsphinx-toctree": {"hidden": True}},'source': ""})
                nb.cells += [toctree]
            
            nb.cells[-1]['source'] += "[%s](%s)\n" % (title, '/'.join(fpath[-2:]))
            nbformat.write(nb, fname, nbformat.NO_CONVERT)
        
# make the root level file the index
os.system("mv docs/_files.ipynb docs/index.ipynb")

print('')
print('done')
