import scrapy,json

from drug.items import DrugDetailsItem

class DrugDetailsSpider(scrapy.Spider):
    name = "drugDetails"
    allowed_domains = ["drugs.com"]
    input_file = "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/all_drug.json"
    start_urls = []
    with open(input_file) as f:
        dict = json.load(f)

        for pair in dict:
            if len(pair["drug_link"]) > 0:

                start_urls.append("https://www.drugs.com" + pair["drug_link"][0])

    def parse(self,response):
        print response.status
        print "\n\n\n\n\n"
        if response.status == 200:
            item = DrugDetailsItem()
            item['drug_name'] = response.xpath("//h1/text()").extract()
            item['detailsOne'] = response.xpath("//div[@class='contentBox']/p[2]/text()").extract()
            item['detailsTwo'] = response.xpath("//div[@class='contentBox']/p[3]/text()").extract()
            yield item
