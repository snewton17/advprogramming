import scrapy


class HomeworkSpider(scrapy.Spider):
    name = "homework"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rank = response.xpath('//td[1]/text()').get()
        company = response.xpath('//td[2]/a/text()').get()
        symbol = response.xpath('//td[3]/a/text()').get()
        ytd_return = response.xpath('//td[4]/text()').get()
        return {"rank": rank, "company": company, "symbol": symbol,
                "ytd_return": ytd_return}
