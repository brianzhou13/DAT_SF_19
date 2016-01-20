import scrapy
from craigslist.items import CraigslistItem

class CraigslistSpider(scrapy.Spider): #extending scrapy.Spider 
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "http://sfbay.craigslist.org/search/sfc/apa"
    ]

    def parse(self, response):  #what is the self and response?
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
            #f.write(response.body)def parse(self, response):

        for sel in response.xpath("//div[@class='content']/span[@class='rows']/p"): #waht is sel?

            item = CraigslistItem()
            item['title'] =  sel.xpath("span/span/a[@class='hdrlnk']").extract()[0] #what does the 0 mean
            #sel.xpath("span/span/a[@class='hdrlnk']").extract()/text()[0] #the text() function will get us text
            item['link']  =  sel.xpath("span/span/a[@class='hdrlnk']/@href").extract()[0]
            #price['price'] = sel.xpath("span[@class='price']").extract()[0]
            yield item #similar to a return command, and it appending all items prior to it: item['title'], item['link']

             # Does the next page exist?  Let's get it!
        next_page   = response.xpath("(//a[@class='button next']/@href)[1]") #after it exhausts all its results, then it'll go to the next-button

        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)