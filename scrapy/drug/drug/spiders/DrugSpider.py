import scrapy,json

from drug.items import DrugItem

class DrugSpider(scrapy.Spider):
    name = "illness"
    allowed_domains = ["drugs.com"]
    start_urls = []
    # index is a - z
    for i in range(0,25):
        start_urls.append("https://www.drugs.com/condition/"+str(unichr(ord('a') + i))+".html")

    def parse(self, response):
        if response.status == 200:
                for sel in response.xpath("//ul[@class='column-list-2']/li"):
                    item = DrugItem()
                    item['illness'] = sel.xpath('a/text()').extract()
                    item['link'] = sel.xpath('a/@href').extract()
                    next_level_url = "https://www.drugs.com"+item['link'][0]

                    yield scrapy.Request(next_level_url, callback = self.parse_condition)
                    # items.append(item)
        # return items

    def parse_condition(self, response):
        if response.status == 200:
            for sel in response.xpath("//tr[@class='condition-table__summary']"):

                item = DrugItem()
                item['illness'] = response.url
                item['drug_link'] = sel.xpath("td[@class='condition-table__drug-name']/span/a/@href").extract()
                item['rx_otc'] = sel.xpath("td[@class='condition-table__rx-otc']/span/text()").extract()
                item['pregnancy'] = sel.xpath("td[@class='condition-table__pregnancy']/span/text()").extract()
                item['csa'] = sel.xpath("td[@class='condition-table__csa']/span/text()").extract()
                item['alcohol'] = sel.xpath("td[@class='condition-table__alcohol']/span/text()").extract()
                item['review_num'] = sel.xpath("td[@class='condition-table__reviews']/a/text()").extract()
                item['rating'] = sel.xpath("td[@class='condition-table__rating']/div/text()").extract()
                item['popularity'] = sel.xpath("td[@class='condition-table__popularity']/div/div/div/span/@style").extract()

                yield item
            #choose top 25 popularity medicine for every illness temporarily
            # int page_num = response.xpath("")

