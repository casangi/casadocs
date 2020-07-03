import os

# toctree pages
header = """
===================================

"""
body = """
.. toctree::
   :hidden:
   :maxdepth: 3

"""


# grab the list of all pages in casadocs
with open('scraper/_sitemap.txt') as fid:
    urls = fid.read().splitlines()

# each page in casadocs should have already been downloaded by the scrapy spider to an html file
# the local html directory structure should match the casadocs website structure
# we will execute pandoc on each of these files to convert their format
for ii, url in enumerate(urls):
    fpath = ['html'] + url.split("/")[4:]
    source = '/'.join(fpath) + '.html'
    if os.path.exists(source):
        print('converting %s of %s...' % (str(ii), str(len(urls))), end='\r')
        
        fpath = ['docs/_files'] + url.split("/")[4:]
        for ii in range(1,len(fpath)):
            subdir = '/'.join(fpath[:ii])
            if not os.path.isdir(subdir):
                os.mkdir(subdir)
        dest = '/'.join(fpath) + '.rst'
        #os.system('pandoc --toc %s -f html -t ipynb -s -o %s' % (source, dest))
        os.system('pandoc --toc %s -f html -t rst -s -o %s' % (source, dest))
        
        # add each file to the toctree of the parent folder
        if len(fpath) > 1:
            fname = '/'.join(fpath[:-1])+'.rst'
            if not os.path.exists(fname):  # if the parent folder doesn't have its own page
                with open(fname, 'w') as fid:
                    fid.write(fpath[-2] + header + body + '   %s' % ('/'.join(fpath[-2:])))
            else:   # see if it already has a toctree
                with open(fname) as fid:
                    lines = fid.read().splitlines()
                if '.. toctree::' not in lines:
                    with open(fname, 'a') as fid:
                        fid.write('\n' + body + '   %s' % ('/'.join(fpath[-2:])))
                else:  # just add this file to the existing toctree
                    with open(fname, 'a') as fid:
                        fid.write('\n   %s' % ('/'.join(fpath[-2:])))
                

# now we just need to create .rst files in the root of each subdirectory to hold the toctrees
#for dir,subdirs,files in os.walk('docs/_files'):
#    rst_body = '%s\n===================================\n\n%s' % (dir.split('/')[-1], body)
#    if len(files) > 0:
#        fs = [file.split('.')[0] for file in files if file != 'index.rst']
#        rst_body = rst_body + "\n   ".join(fs) + "\n   "
#    if len(subdirs) > 0:
#        rst_body = rst_body + "/index.rst\n   ".join(subdirs) + "/index.rst\n"
#    with open(dir+'/index.rst', 'w') as fid:
#        fid.write(rst_body)

print('done')
