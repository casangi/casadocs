import scrapy


class SitemapSpider(scrapy.Spider):
    name = "sitemap"

    def start_requests(self):
        urls = ['https://casa.nrao.edu/casadocs-devel/sitemap']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        body = '\n'.join(response.css("#content a::attr(href)").getall())
        with open('scraper/_sitemap.txt', 'w') as fid:
            fid.write(body)
        self.log('generated _sitemap.txt')
