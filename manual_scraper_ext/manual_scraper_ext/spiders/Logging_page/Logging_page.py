import scrapy


class LoggingPageSpider(scrapy.Spider):
    name = "Logging_page"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        inputs = response.css('form input')
        print(inputs)

        formdata = {}
        for input in inputs:
            name = input.css('::attr(type)').get()
            value = input.css('::attr(value)').get()
            formdata[name] = value

        formdata['username'] = 'YOUR_USERNAME'
        formdata['password'] = 'YOUR_PASSWORD'

        return scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.parse_after_login
        )

    def parse_after_login(self, response):
        print(response.xpath('.//div[@class = "col-md-4"]/p/a/text()').get())