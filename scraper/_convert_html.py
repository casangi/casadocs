import os
import re
import nbformat

# toctree pages
toctree = """
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
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging']
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean']
#url = urls[0]

# each page in casadocs should have already been downloaded by the scrapy spider to an html file
# the local html directory structure should match the casadocs website structure
# we will execute pandoc on each of these files to convert their format
for ii, url in enumerate(urls):
    fpath = ['html'] + url.split("/")[4:]
    folder = os.path.isdir('/'.join(fpath))  # turn folders in to rst files with toctrees

    # dont process extra task and tool pages for now
    if ('global-task-list' in fpath) and (('planning' in fpath) or ('developer' in fpath) or ('about' in fpath)): continue
    if ('global-tool-list' in fpath) and (('planning' in fpath) or ('developer' in fpath) or ('about' in fpath)): continue

    source = '/'.join(fpath) + '.html'
    if os.path.exists(source):
        print('converting %s of %s...' % (str(ii), str(len(urls))), end='\r')
        
        spath = ['docs', '_files'] + url.split("/")[5:]
        for ii in range(1,len(spath)):
            subdir = '/'.join(spath[:ii])
            if not os.path.isdir(subdir):
                os.mkdir(subdir)
        dest = '/'.join(spath)
        
        # use pandoc to convert html to either ipynb or rst format
        # rst is used for folders to hold toctrees
        if folder or ('global-task-list' in fpath) or ('global-tool-list' in fpath):
            os.system('pandoc %s -f html -t rst -o %s --extract-media=%s' % (source, dest+'.rst', '/'.join(spath[:-1])))

            with open(dest+'.rst', 'r') as fid:
                rst = fid.read()

            # cleanup some conversion messiness
            rst = rst.replace('\\ ', ' ')
            rst = rst.replace('.. container::\n   :name: viewlet-above-content-title\n\n', '')
            rst = rst.replace('.. container::\n   :name: viewlet-below-content-title\n\n', '')
            rst = rst.replace('.. container:: section\n   :name: viewlet-above-content-body\n\n', '')
            rst = rst.replace('.. container:: section\n   :name: viewlet-below-content-body\n\n', '')
            rst = rst.replace('/'.join(spath[:-1])+'/', '')

            subdirs = [uu.split('/')[-1] for uu in urls if re.search('%s/[^/]+$'%fpath[-1], uu)]
            if len(subdirs) > 0:
                rst += toctree
                for entry in subdirs:
                    if ('global-task-list' in fpath) and (entry in ['about', 'planning', 'developer']): continue
                    if ('global-tool-list' in fpath) and (entry in ['about', 'planning', 'developer']): continue
                    rst += "   %s/%s\n" % (spath[-1], entry)

            with open(dest + '.rst', 'w') as fid:
                fid.write(rst)

        # otherwise use ipynb format for easier content editing later on
        else:
            os.system('pandoc %s -s -f html -t ipynb -o %s --atx-headers --extract-media=%s' % (source, dest+'.ipynb', '/'.join(spath[:-1])))

            # now we need to manually fix the notebook to conform to nbsphinx conversion limitations
            nb = nbformat.read(dest+'.ipynb', nbformat.NO_CONVERT)
            md = nb.cells[0]['source']

            # get rid of extraneous span tags
            md = re.sub('<span(.|\n)*?>','', md)
            md = re.sub('</span>', '', md)

            # fix image links to work properly from notebooks
            md = re.sub('<img src="(.+?)" .+?/>', r'![\1](\1)', md)
            md = re.sub('attachment:%s/'%'/'.join(spath[:-1]), '', md)

            # split sections in to separate cells at appropriate level
            splits = re.split(r'(#+\s)', md)[1:]
            for ii in range(0, len(splits), 2):
                if ii == 0:
                    nb.cells[0] = nbformat.v4.new_markdown_cell(splits[0]+splits[1])
                else:
                    nb.cells += [nbformat.v4.new_markdown_cell('#'+splits[ii]+splits[ii+1])]

            nbformat.write(nb, dest+'.ipynb', nbformat.NO_CONVERT)

        # we need to extract the proper title
        # with open(source, 'r') as fid:
        #     lines = fid.read()
        # title = re.search('<h1 class="documentFirstHeading">(.+?)</h1>', lines).group(1)

        ## add each file to the toctree of the parent folder
        #fname = '/'.join(spath[:-1]) + '.ipynb'
        #nb = nbformat.read(fname, nbformat.NO_CONVERT)
        #
        ## the last cell should be the toctree, if not, create a new cell with one
        #if 'nbsphinx-toctree' not in nb.cells[-1]['metadata']:
        #    toctree = nbformat.from_dict({'cell_type': 'markdown', 'metadata': {"nbsphinx-toctree": {"hidden": True}},'source': ""})
        #    nb.cells += [toctree]
        #
        #nb.cells[-1]['source'] += "[%s](%s)\n" % (title, '/'.join(spath[-2:]))
        #nbformat.write(nb, fname, nbformat.NO_CONVERT)
        
# make the root level file the index
os.system("mv docs/_files.rst docs/index.rst")

print('')
print('done')
