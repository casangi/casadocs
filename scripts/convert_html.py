##################################################################################
# converts downloaded Plone html pages to markdown for Jupyter notebook cells or
# restructuredText format for directory trees and the task / tool pages
##################################################################################

import os
import re

# grab the list of all pages in casadocs
with open('scraper/_sitemap.txt') as fid:
    urls = fid.read().splitlines()
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam']
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export/uv-data-import']
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean']
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/using-plotms-to-plot-and-edit-visibilities-and-calibration-tables']
#urls = ['https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset']
#url = urls[0]

os.system('rm -fr markdown')
os.system('rm -fr docs/tasks')
os.system('mkdir markdown')
os.system('mkdir docs/tasks')

# each page in casadocs should have already been downloaded by the scrapy spider to an html file
# the local html directory structure should  match the casadocs website structure
# we will execute pandoc on each of these files to convert their format
for ii, url in enumerate(urls):
    fpath = ['html'] + url.split("/")[4:]
    if url.endswith('global-task-list') or (re.match('.*/global-task-list/task_\S*/.+', url) is not None): continue
    if url.endswith('global-tool-list') or (re.match('.*/global-tool-list/tool_\S*/.+', url) is not None): continue
    if 'stable' not in url: continue   # ignore root directory test files
    
    source = '/'.join(fpath) + '.html'
    if os.path.exists(source):
        print('converting %s of %s...' % (str(ii), str(len(urls))), end='\r')

        if 'global-task-list' in fpath:
            dest = 'docs/tasks/' + url.split("/")[-1]
        else:
            spath = ['markdown'] + url.split("/")[5:]
            for ii in range(1,len(spath)):
                subdir = '/'.join(spath[:ii])
                if not os.path.isdir(subdir):
                    os.mkdir(subdir)
            dest = '/'.join(spath)
            dest = 'markdown/index' if dest == 'markdown' else dest
        
        # use pandoc to convert html to either ipynb or rst format
        # rst is used for task / tool descriptions that are later turned in to docstrings
        # the top level markdown/index file is from html/stable and forms the index.rst later on
        if ('global-task-list' in fpath) or ('global-tool-list' in fpath) or (dest == 'markdown/index'):
            # merge some of the individual task pages
            fullrst = ''
            for head, suffix in [('Description',''), ('Examples', '/examples'), ('Development','/developer')]:
                tsrc = source.replace('.html', suffix+'.html')
                if not os.path.exists(tsrc): continue
                os.system('pandoc %s -f html -t rst -o %s --extract-media=%s' % (tsrc, dest+'.rst', 'docs/tasks/_apimedia'))
                with open(dest+'.rst', 'r') as fid:
                    rst = fid.read()

                # convert to sphinx boxes
                rst = re.sub('(\s*)\.\. container:: casa-\S*-box', r'\1::', rst, flags=re.DOTALL)  # change code boxes
                rst = re.sub('(\s*)\.\. container:: terminal-box', r'\1::', rst, flags=re.DOTALL)  # change terminal boxes
                rst = re.sub('(\s*)\.\. container:: alert-box\s*', r'\1.. warning:: ', rst, flags=re.DOTALL)  # change alert boxes
                rst = re.sub('(\s*)\.\. container:: \S*-box\s*', r'\1.. note:: ', rst, flags=re.DOTALL)  # change info boxes

                # remove containers and de-indent text below
                for ii in range(10):
                    for blob in re.finditer('(?<=\n).. container::.*?\n\n   (.*?\n\n)(?=\S)', rst, flags=re.DOTALL):
                        rst = rst.replace(blob.group(0), blob.group(1).replace('\n   ','\n'))
                
                # remove remaining container sections
                rst = re.sub('\s*\.\. container::(\s*\S*)*?\n(\s*:name: \S*\n)?', '\n', rst, flags=re.DOTALL)
            
                # rubrics don't need names and classes
                rst = re.sub('(\s*\.\. rubric::.*?)(:name: \S*)?\s*(:class: \S*)?\n\s*?\n', r'\1\n\n', rst, flags=re.DOTALL)
                rst = re.sub('(\s*)\.\. rubric::\s*\n\n', r'\1\n\n', rst, flags=re.DOTALL)  # remove empty rubrics
                
                rst = rst.replace(' ', ' ').replace('\\ ', ' ').replace('↩ ', '')  # weird ascii things
                rst = re.sub('(:math:\s*`[^\n]+) `', r'\1`', rst, flags=re.DOTALL)  # fix math equations with trailing space before `
                rst = re.sub('\s*[\+\-]+\n\s*\| Citation.*?\n\n', '\n\n', rst, flags=re.DOTALL)  # remove citation tables
                rst = re.sub('\n\s+Bibliography\s*\n', '\n\n\n   Bibliography\n', rst, flags=re.DOTALL)  # fix bibliography indent
                
                # fix image links and get rid of image attributes, they don't work with Sphinx
                rst = re.sub('(\.\. \|.*?\| image:: )docs/tasks/_apimedia/(\S*)\s*?\n', r'\1_apimedia/\2\n', rst, flags=re.DOTALL)
                rst = re.sub('\n\s*:class:.*?\n', r'\n', rst, flags=re.DOTALL)
                rst = re.sub('\n\s*:width:.*?\n', r'\n', rst, flags=re.DOTALL)
                rst = re.sub('\n\s*:height:.*?\n', r'\n', rst, flags=re.DOTALL)

                # create heading
                header = '\n\n.. _%s:\n\n%s\n   ' % (head, head)
                if re.search('(\n\S+\n=+\n+)(.*)', rst, flags=re.DOTALL):
                    rst = header + re.search('(\n\S+\n=+\n+)(.*)', rst, flags=re.DOTALL).group(2).replace('\n','\n   ')
                else:
                    rst = header + rst.strip().replace('\n','\n   ')
                
                # tack on the end
                fullrst = fullrst + rst

            with open(dest + '.rst', 'w') as fid:
                fid.write(fullrst)
            
        # otherwise use ipynb format for easier content editing later on
        else:
            os.system('pandoc %s -f html -t markdown-grid_tables -o %s --wrap=none --atx-headers --extract-media=%s' % (source, dest+'.md', 'markdown/_media')) #'/'.join(spath[:-1])))
            
            with open(dest+r'.md', 'r') as fid:
                md = fid.read()
            
            # clean up citations
            md = re.sub('\(#cit.*?\){.*?}', '(#Bibliography)', md)
            md = re.sub(' +\-{17} \-+.*?\-{17} \-+', '', md, flags=re.DOTALL)
            md = re.sub('<table class=\"citation\-table\">.*?</table>', '', md, flags=re.DOTALL)
            md = re.sub('::: {#citation-title}\s*Bibliography\s*:::\s*', ':::\n# Bibliography\n:::\n', md, flags=re.DOTALL)
            for bib in re.finditer(':::\n# Bibliography\n:::\n(.*?):::\s*:::', md, flags=re.DOTALL):
                txt = re.sub('\s*</?div>\s*', '', bib.group(1), flags=re.DOTALL).replace('\n', ' ')
                txt = re.sub(r'\W*\^(\d\.)[\\\^\s]+(.+?)\[.*?\]\(#ref.*?\)', r'\1 \2\n', txt)
                md = md.replace(bib.group(1), txt)
            
            # clean simple tables
            for tgp in re.finditer('::: {.table\-wrap}(.*?):::', md, flags=re.DOTALL):
                md = md.replace(tgp.group(1), re.sub(r'\[([^\]]*?)\]\{style.*?\}',
                                                     lambda m: m.group(1)+' '*(len(m.group(0))-len(m.group(1))),
                                                     tgp.group(1), flags=re.DOTALL))
            
            # remove escapes, <div> tags, and heading symbols from code blocks
            for bs in ['casa-input-box', 'terminal-box', 'casa-output-box', 'info-box', 'alert-box']:
                for tgp in re.finditer('::: {\.%s}(.*?):::'%bs, md, flags=re.DOTALL):
                    submd = re.sub(r'\\(?!n)', '', tgp.group(1))
                    submd = re.sub('#[^\S\n]+', '#', submd, flags=re.DOTALL)
                    submd = re.sub('</?div>', '', submd, flags=re.DOTALL)
                    md = md.replace(tgp.group(1), submd)
            
            # convert the various text boxes
            md = re.sub('::: {.info-box}(.*?):::\n', r'<div class="alert alert-info">\1</div>\n', md, flags=re.DOTALL)
            md = re.sub('::: {.alert-box}(.*?):::\n', r'<div class="alert alert-warning">\1</div>\n', md, flags=re.DOTALL)
            md = re.sub('::: {.casa-input-box}(.*?):::\n', r'```\1```\n', md, flags=re.DOTALL)
            md = re.sub('::: {.terminal-box}(.*?):::\n', r'```\1```\n', md, flags=re.DOTALL)
            md = re.sub('::: {.casa-output-box}(.*?):::\n', r'```python\1```\n', md, flags=re.DOTALL)
            md = re.sub(':::.*', '', md)
            
            # weird ascii things
            md = md.replace(' ', ' ').replace('\\\n', '')
            md = re.sub('\n\n\n+', '\n\n', md, flags=re.DOTALL)
            md = re.sub('(\S+)\n(\-+)\n', r'\1\n\n\2\n', md, flags=re.DOTALL)   # preserve horizontal rules after removing stray / chars
            
            # get rid of remaining weird style tags
            md = re.sub(r'\[([^\]]*?)\]\{(\.s1)?\s?(style)?.*?\}', r'\1', md, flags=re.DOTALL)
            md = re.sub(r'\[([^\]]*?)\]\{(\.s1)?\s?(style)?.*?\}', r'\1', md, flags=re.DOTALL) # do a couple times for nested things
            md = re.sub(r'\[([^\]]*?)\]\{(\.s1)?\s?(style)?.*?\}', r'\1', md, flags=re.DOTALL)
            md = re.sub(r'\{\.s1.*?\}|\{style.*?\}', '', md, flags=re.DOTALL) # kill remaining dangling style tags
            #md = re.sub(r'\[([^\n]+)\]\{(\.s1)?\s?(style)?.*?\}', r'\1', md, flags=re.DOTALL)
            #md = re.sub(r'\[([^\n]+)\]\{(\.s1)?\s?(style)?.*?\}', r'\1', md, flags=re.DOTALL) # do a couple times for nested things
            md = re.sub('{.*? \.documentFirstHeading}', '', md)
            md = re.sub('(\n#+ [^\n]*)\{.*?\}', r'\1', md, flags=re.DOTALL)  # bracketing in headers must go
            md = re.sub('\n#+ +\n', '\n', md, flags=re.DOTALL)  # some headers end up empty after previous cleanup
            
            # fix image links to work properly from notebooks
            md = re.sub('!\[.*?]\(\S*?/(\w*)(\.\w*).*?\)', r'![\1](media/\1\2)', md, flags=re.DOTALL)
            
            # fix image captions
            md = re.sub(' +\-{9} \-+.*?Caption\s*(.*?)\-{9} \-+', r'>\1', md, flags=re.DOTALL)
            
            with open(dest+r'.md', 'w') as fid:
                fid.write(md)

print('')
print('done')
