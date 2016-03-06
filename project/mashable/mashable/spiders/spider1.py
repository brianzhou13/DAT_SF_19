
import pandas as pandas
import numpy as numpy

import scrapy
from mashable.items import MashableItem 


from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class MashableSpider(scrapy.Spider):
	name = "dmoz" #placeholder for spider na

	allowed_domains = ["mashable.org"] #["dmoz.org"]

	start_urls = MashableItem.mash_url_only #needs a list, we have it to 100 urls

	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)

		item = MashableItem()
	

		item['url'] = response.url
		item['h1'] = response.xpath('//header[@class = "article-header"]/h1/text()').extract()
		item['title'] = response.xpath('//title/text()').extract()
		item['description'] = response.xpath('//head/meta[@name = "keywords"]/@content').extract()
		item['author'] = response.xpath('//head/meta[@name = "sailthru.author"]/@content').extract()
		item['body_content'] = response.xpath('//section[@class= "article-content"]').extract()
		#Deal with this later as we dive further into our project 
			#only pulling back the h1 right now; and nothing else

		yield item


	#def parse(self, response):
	#	for sel in response.xpath():
	#		item = DanishItem()