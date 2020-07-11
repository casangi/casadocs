import scrapy
from scrapy_splash import SplashRequest
import os
import re

rst_body = """.. toctree::
   :hidden:
   :maxdepth: 2
   :glob:


"""


class CasadocsSpider(scrapy.Spider):
    name = "single"
    
    def start_requests(self):
        urls = ['https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging']
        
        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
            yield SplashRequest(url, self.parse, endpoint='render.html', args={'wait': 2.0}, )
    
    def parse(self, response):
        fpath = ['html'] + response.url.split("/")[4:]
        
        # some plone pages have automatic redirects elsewhere, we need to get around that
        if 'redirect_urls' in response.request.meta.keys():
            fpath = ['html'] + response.request.meta['redirect_urls'][0].split("/")[4:]
        
        for ii in range(1, len(fpath)):
            if not os.path.isdir('/'.join(fpath[:ii])):
                os.mkdir('/'.join(fpath[:ii]))
        
        # filename comes from the url to preserve the sitemap
        filename = '%s.html' % '/'.join(fpath)
        
        # title comes from the navigation tree, can't trust the url or page header
        title = ''.join(response.css("a.navTreeCurrentItem::text").getall()).strip()
        
        # now of course with task and tool redirects, the title may need to be adjusted again
        if fpath[-1].startswith('task_') or fpath[-1].startswith('tool_'):
            title = fpath[-1][5:]
        
        # main HTML of page
        body = ''.join(response.css("#content").getall())  #.css("#parent-fieldname-text").getall())
        
        # stick a proper heading back on top
        #body = ("<!DOCTYPE html>\n <head><title>%s</title></head>\n" % title) + body
        
        # the main heading of the page is used later to set the new navigation and page name
        # sometimes the plone heading differs from the plone navigation tree, and the navigation tree is a better name
        # so here we overwrite the heading with whatever the navigation tree is calling this page
        body = re.sub('(<h1 class="documentFirstHeading">).*(</h1>)', r'\1%s\2' % title, body)
        
        # plone folders/pages that list contents need to be removed, they will be replaced by toctrees and their links are bad anyway
        entries = response.css('div.entries').getall()
        if len(entries) > 0:
            body = body.replace(''.join(entries), '')
        
        # for some reason, mathjax has duplicative information that needs to be removed
        # entries = response.css("span[class*=mjx]").getall()
        # entries += response.css("span[class*=MJXp]").getall()
        entries = response.css("span.mjx-chtml").getall()
        for entry in entries:
            body = body.replace(entry, '')
        
        with open(filename, 'w') as fid:
            fid.write(body)
        self.log('Saved file %s' % filename)
