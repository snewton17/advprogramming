import scrapy


class HomeworkLoopSpider(scrapy.Spider):
    name = "homework_loop"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rows = response.xpath('//div[@class="container-fluid mt-4 maxWidth"]//table/tbody/tr')
        for row in rows:
            rank = row.xpath('./td[1]/text()').get()
            company = row.xpath('./td[2]/a/text()').get()
            symbol = row.xpath('./td[3]/a/text()').get()
            ytd_return = row.xpath('./td[4]/text()').get().strip()

            yield {
                "rank": rank,
                "company": company,
                "symbol": symbol,
                "ytd_return": ytd_return
            }



