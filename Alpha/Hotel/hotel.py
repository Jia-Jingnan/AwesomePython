# Author:   jingnan
# Date:    2021/7/4
# Desc:
import requests


class HttpRequest:

    # 初始化方法
    def __init__(self, url, data):
        self.url = url
        self.data = data


    '''
    完成http请求
    '''
    def get_request(self, url, data):
        res = requests.get(url, data)
        print('返回结果:', res)


    # 实例方法,只能由实例调用
    def post_request(self, url, data):
        res = requests.post(url, data)
        print('返回结果：', res)

    @staticmethod
    def first_call():
        print('先调用的静态方法')


    @classmethod
    def add(cls):
        print('类方法')


HttpRequest.add()

httpRequest = HttpRequest('123', '123132')
httpRequest.post_request()