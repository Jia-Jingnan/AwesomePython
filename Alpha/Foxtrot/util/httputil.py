# Author:   jingnan
# Date:    2021/6/20
# Desc:

import requests

class HttpRequest:
    '''
    利用requests封装get请求和post请求
    :param url 请求的url地址
    :param data 请求要发送的数据
    :param cookie 请求要携带的cookie
    '''

    def request(self,method, url, data, cookie=None):
        if method.lower() == 'post':
            # 传application/json格式的数据使用 json = '{}'
            res = requests.post(url, data)
            return res
        if method.lower() == 'get':
            res = requests.get(url,data)
            return res




if __name__ == '__main__':
    url = 'http://localhost:8089/user/login.do'

    # 默认是application/x-form-data
    data = {'username': 'admin', 'password': 'admin'}
    HttpRequest().request(url, data)

