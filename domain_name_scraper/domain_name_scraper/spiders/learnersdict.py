'''
@author: kim
'''
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.conf import settings

from domain_name_scraper.items import DomainNameScraperItem


class LearnersDictPopularSpider(CrawlSpider):
    name = "learnerspop"
    allowed_domains = ["learnersdictionary.com"]
    start_urls = [
        "http://www.learnersdictionary.com/most-popular-words",
    ]
    
    rules = (Rule(LinkExtractor(allow=('definition', )), callback="parse_items", follow=True),)
    
    
    settings.overrides['DEPTH_LIMIT'] = 1
    

    def parse_items(self, response):
        """
        
        """
        sel = Selector(response)
        items = []
        
        if "learnersdictionary.com/definition" not in response.url:
            return items
        #sites = sel.xpath("//div[@class='entry entry_v2 boxy']")
        sites = sel.css('div.entry')
        for site in sites:
            item = DomainNameScraperItem()
            item['word'] = site.css('span.hw_txt::text').extract()
            try:
                item["word"] = str(list(item["word"])[-1]).strip()
            except: return items
            if not item["word"]:return items
            item['meaning'] = site.xpath('.//div[@class="sense"]/span[@class="def_text"]/text()').extract()
            item['example'] = ""
            item['pos'] = ""
            item['neg'] = ""
            item["source"]="learnersdict_popular"
            items.append(item)
        return items