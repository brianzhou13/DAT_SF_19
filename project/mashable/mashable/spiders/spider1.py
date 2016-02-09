
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
		
		#for sel in response.xpath('//body[@class='body_posts body_show']/div[@id='peek']/div[@id='scrollable']/div[@id='body-container']/div[@id='main']/div[@class='page-container']/div[@id='body']/div[@class='flex-box']/div[@class='box-cell']/div[@id='post-content']/div[@id='post-slider']/article[@id='story']/header[@class='article-header']/h1[@class='title']').extract():
		
		#for sel in response:
		#removing the above for loop since we are only 'one-time' pulling elements from our page

		item['url'] = response.url
		item['h1'] = response.xpath('//header[@class = "article-header"]/h1/text()').extract()
		item['title'] = response.xpath('//title/text()').extract()
		item['description'] = response.xpath('//head/meta[@name = "keywords"]/@content').extract()
		item['author'] = response.xpath('//head/meta[@name = "sailthru.author"]/@content').extract()
			#only pulling back the h1 right now; and nothing else


		yield item


	#def parse(self, response):
	#	for sel in response.xpath():
	#		item = DanishItem()