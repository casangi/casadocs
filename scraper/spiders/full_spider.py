import scrapy
import os

rst_body = """.. toctree::
   :hidden:
   :maxdepth: 2
   :glob:

   
"""

class CasadocsSpider(scrapy.Spider):
    name = "full"

    def start_requests(self):
        with open('scraper/_sitemap.txt') as fid:
            urls = fid.read().splitlines()
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fpath = ['html'] + response.url.split("/")[4:]
        for ii in range(1,len(fpath)):
            if not os.path.isdir('/'.join(fpath[:ii])):
                os.mkdir('/'.join(fpath[:ii]))
        
        # only process actual pages, skip folders
        #if (len(response.css("body.portaltype-document")) > 0) or (len(response.css("div.entries")) == 0):
        filename = '%s.html' % '/'.join(fpath)
        body = ''.join(response.css("#content").getall())
        with open(filename, 'w') as fid:
            fid.write(body)
        self.log('Saved file %s' % filename)
