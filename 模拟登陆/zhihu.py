# coding = utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest


class ZhihuSpider(CrawlSpider):
    name = 'zhspider'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        login_url = 'https://www.zhihu.com/login'
        return [Request(login_url, method='get', callback=self.post_login)]

    def post_login(self, response):
#=========================================================================================================
        xsrf = HtmlXPathSelector(response).select('//input[@name="_xsrf"]/@value').extract()[0]
        formdata = {'_xsrf': xsrf, 'next': 'http://www.zhihu.com/people/cha-men-hu-de-xiao-bei-xin/answers',
                    'email': '******', 'password': '********'}
        return [FormRequest(url='https://www.zhihu.com/login', formdata=formdata, callback=self.parse_item)]
#=========================================================================================================
    def parse_item(self, response):
        print response.body
        hxs = HtmlXPathSelector(response)
        # questions = []
        # for ele in hxs.select('//div[@class="zm-item"]'):
        question = QuestionItem()
        question['QuestionLink'] = hxs.select('//div[@class="zm-item"]//a[@class="question_link"]/@href').extract()
        question['Question'] = hxs.select('//div[@class="zm-item"]//a[@class="question_link"]/text()').extract()
        question['Votes'] = hxs.select( '//div[@class="zm-item"]//div[@class="zm-item-vote-info "]/@data-votecount').extract()
        question['Answer'] = hxs.select('//div[@class="zm-item"]//div[@class="zm-editable-content clearfix"]/text()').extract()
        # print question['Votes']

        return question