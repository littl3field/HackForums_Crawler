# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Spider
from scrapy.http import Request, response
from scrapy.http import FormRequest
from scrapy.selector import Selector
from hackforums.items import HackforumsItem
from scrapy.loader import ItemLoader
from scrapy.utils.response import open_in_browser
from scrapy.selector import HtmlXPathSelector


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['hackforums.com']
    start_urls = ['https://hackforums.net/forumdisplay.php?fid=92']

    def parse(self, response):
        hack = response.xpath('//*[@id="container"]')
        post_title = response.xpath('//*[@class=" subject_new"]/a/text()')
        post_time = response.xpath('//*[@class="lastpost smalltext"]/text()')
        post_lastpost = response.xpath('//*[@class="lastpost smalltext"]/a/text()')
        post_author = response.xpath('//*[@class="author smalltext"]/a/text()')
        post_link = response.xpath('//*[@class=" subject_new"]/a/@href')
        items = []
        for post_title, post_time, post_author, post_lastpost, post_link in zip(post_title, post_time, post_author, post_lastpost, post_link):
            item = HackforumsItem()
            item['Title'] = re.sub(r'[^a-z A-Z0-9?]', '', post_title.extract().strip())
            item['Title'] = post_time.extract().strip()
            item['Lastpost'] = post_lastpost.extract().strip()
            item['Author'] = post_author.extract().strip()
            item['Link'] = post_link.extract().strip()
            items.append(item)
            yield item

        next_page_url = response.xpath().extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url, callback=self.parse)
