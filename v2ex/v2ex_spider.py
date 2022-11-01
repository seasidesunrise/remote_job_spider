"""
 
:Author:  逍遥游
:Create:  2022/7/10$ 08:53$
"""

import time

from parsel import Selector

from utils.base_spider import Spider
from utils.im_util import log_and_send_im

url = "https://shixian.com/job/all"
post_title = ''

while True:
    spider = Spider(spider_name='ShixianSpider')
    response = spider.requests(method='get', url=url)

    html = Selector(response.text)
    items = html.css('.title')
    print(len(items))
    item = items[0]

    title = item.xpath('.// text()').get()
    if title is None:
        log_and_send_im(f"实现网 爬虫抓取数据异常，请检查！！")
    else:
        title = title.strip()
        if post_title != title:
            print(response.text)
            log_and_send_im(f"实现网 有新的职位信息: {title} {url}")
            post_title = title
    time.sleep(16 * 60)
