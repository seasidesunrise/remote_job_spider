"""
 
:Author:  逍遥游
:Create:  2022/7/7$ 22:28$
"""
import urllib
from abc import ABCMeta

import requests
from requests.adapters import HTTPAdapter
from tenacity import retry, stop_after_attempt, wait_random


class Spider(metaclass=ABCMeta):
    def __init__(self, spider_name, *args, **kwargs):
        # 会话对象
        self.session = requests.session()
        # 设置重试次数
        self.session.mount('http://', HTTPAdapter(max_retries=5))
        self.session.mount('https://', HTTPAdapter(max_retries=5))

    @retry(stop=(stop_after_attempt(5)), wait=wait_random(min=0.2, max=1))
    def requests(self, method: str, url: str, timeout: int = 10, **kwargs) -> requests.Response:
        """
        网络请求方法 封装重试
        """
        try:
            response = self.session.request(method, url, timeout=timeout, **kwargs)
            if response.status_code == 403:
                error = f'对方服务器拒绝请求(403)，可能ip被封或者rate limiter起效 url: {url}'
                raise Exception(error)
            return response
        except Exception as err:
            self.logger.e(f'请求[{url}]失败，失败原因: {str(err)}，args: {kwargs}')

    @staticmethod
    def parse_params(link: str):
        """
        提取链接中的参数
        :param link:
        :return:
        """
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(link).query))

        return query
