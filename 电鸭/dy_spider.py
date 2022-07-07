"""
电鸭招聘只有一个url

原理：
抓取电鸭对应的url，

:Author:  逍遥游
:Create:  2022/7/7$ 21:21$
"""
import time

from parsel import Selector

from utils.base_spider import Spider
from utils.im_util import log_and_send_im

url = "https://eleduck.com/categories/5?sort=new"
post_id = ''

while True:
    spider = Spider(spider_name='DySpider')
    response = spider.requests(method='get', url=url)
    print(response.text)

    html = Selector(response.text)
    items = html.css('.post-title')
    print(len(items))
    item = items[0]

    pid = item.xpath('.// a/@href').get()
    title = item.xpath('.// a/text()').get()
    print(pid)
    if pid != post_id:
        log_and_send_im(f"电鸭有新的职位信息: {pid} {title} {url}")
        post_id = pid
    time.sleep(15 * 60)
