"""
 
:Author:  逍遥游
:Create:  2022/7/7$ 23:01$
"""

import json
import sys

import requests

from utils.spider_cst import *


def send_feishu_msg(text):
    # 定义要发送的数据
    data = {
        "msg_type": "text",
        "content": {"text": text + '\n'}
    }
    # 发送post请求
    try:
        requests.post(webhook, data=json.dumps(data), headers=headers)
    except:
        print("Unexpected error:", sys.exc_info()[0])


def send_feishu_and_set_cache(key, content, cache, cache_mins):
    if cache.get(key) != 1:
        send_feishu_msg(content)
        cache.set(key, 1, ttl=cache_mins * 60)


def log_and_send_im(text):
    """
    输出日志，并发送IM消息
    :param text: 消息内容
    :type text: str
    """
    print(text)
    send_feishu_msg(text)


if __name__ == '__main__':
    send_feishu_msg("bbb")
