'''
        Created on Aug 29, 2015
        
        @author: kim
'''
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor

from domain_name_scraper.items import DomainNameScraperItem


class UrbanDictSpider(CrawlSpider):
    name = "urbandict"
    allowed_domains = ["urbandictionary.com"]
    start_urls = [
        "http://www.urbandictionary.com/",
        "http://www.urbandictionary.com/popular.php?character=Q",
        "http://www.urbandictionary.com/popular.php?character=W",
        "http://www.urbandictionary.com/popular.php?character=E",
        "http://www.urbandictionary.com/popular.php?character=R",
        "http://www.urbandictionary.com/popular.php?character=T",
        "http://www.urbandictionary.com/popular.php?character=Y",
        "http://www.urbandictionary.com/popular.php?character=U",
        "http://www.urbandictionary.com/popular.php?character=I",
        "http://www.urbandictionary.com/popular.php?character=O",
        "http://www.urbandictionary.com/popular.php?character=P",
        "http://www.urbandictionary.com/popular.php?character=A",
        "http://www.urbandictionary.com/popular.php?character=S",
        "http://www.urbandictionary.com/popular.php?character=D",
        "http://www.urbandictionary.com/popular.php?character=F",
        "http://www.urbandictionary.com/popular.php?character=G",
        "http://www.urbandictionary.com/popular.php?character=H",
        "http://www.urbandictionary.com/popular.php?character=J",
        "http://www.urbandictionary.com/popular.php?character=K",
        "http://www.urbandictionary.com/popular.php?character=L",
        "http://www.urbandictionary.com/popular.php?character=Z",
        "http://www.urbandictionary.com/popular.php?character=X",
        "http://www.urbandictionary.com/popular.php?character=C",
        "http://www.urbandictionary.com/popular.php?character=V",
        "http://www.urbandictionary.com/popular.php?character=B",
        "http://www.urbandictionary.com/popular.php?character=N",
        "http://www.urbandictionary.com/popular.php?character=M",
        "http://www.urbandictionary.com/yesterday.php",      
        
    ]
    
    rules = (Rule(LinkExtractor(allow=("browse","popular","yesterday","define","favorites" )), callback="parse_items", follow=True),)
    

    def parse_items(self, response):
        """
        
        """
        sel = Selector(response)
        items = []
        
        """if "urbandictionary.com/define" not in response.url:
            return items"""
        
        sites = sel.xpath('//div[@id="content"]/div[@class="def-panel"][1]')
        for site in sites:
            item = DomainNameScraperItem()
            item['word'] = site.xpath('div[@class="def-header"]/a[@class="word"]/text()').extract()
            item['meaning'] = site.xpath('div[@class="meaning"]/text()').extract()
            item['example'] = site.xpath('div[@class="example"]/text()').extract()
            item['pos'] = site.xpath('.//a[@class="thumb up"]/span[@class="count"]/text()').extract()
            item['neg'] = site.xpath('.//a[@class="thumb down"]/span[@class="count"]/text()').extract()
            item["source"]="urbandictonary"
            items.append(item)

        return items