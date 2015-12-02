from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from Scrapy_tutorial_wiki.items import TutorialWikiItem



class TutorialWikiSpider(Spider):
    name = 'TutowikiSpider'
    alloed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report"]

    def parse(self,response):
        sel = HtmlXPathSelector(response)
        item = TutorialWikiItem()
        item['rank'] = sel.select('//table[@class="wikitable"]/tr/td[1]/text ()').extract()
        item['article'] = sel.select('//table[@class="wikitable"]/tr/td[2]/a[@title]/text()').extract()
        item['link'] =sel.select('//table[@class="wikitable"]/tr/td[2]/a/@href').extract()
        item['views'] = sel.select('//table[@class="wikitable"]/tr/td[4]/text ()').extract()
        item['periode'] = sel.select('//div[@class="mw-content-ltr"]/h1/span[@class="mw-headline"]/text()').extract()

        return item
