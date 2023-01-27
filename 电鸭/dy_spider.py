"""
电鸭招聘只有一个url

原理：
抓取电鸭对应的url，

:Author:  逍遥游
:Create:  2022/7/7$ 21:21$
"""
import time

from parsel import Selector
import json
from utils.base_spider import Spider
from utils.im_util import log_and_send_im

url = "https://eleduck.com/categories/5?sort=new"
last_post_id = ''
last_title = ''

while True:
    spider = Spider(spider_name='DySpider')
    response = spider.requests(method='get', url=url)

    html = Selector(response.text)
    items_json_text = html.css('#__NEXT_DATA__ ::text').get()
    items_dict = json.loads(items_json_text)

    items = items_dict['props']['initialProps']['pageProps']['postList']['posts']
    print(len(items))
    item = items[0]

    pid = item.get('id')
    title = item.get('title')
    print(pid, title)
    print(f"pid: {pid}, title: {title}")
    print(f"last_post_id: {last_post_id}, last_title: {last_title}")
    if pid != last_post_id and title != last_title:
        # print(response.text)
        log_and_send_im(f"电鸭 有新的职位信息: {pid} {title} {url}")
        last_post_id = pid
        last_title = title
    else:
        print(f"重复的工作，忽略")
    time.sleep(5 * 60)
