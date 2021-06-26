# Author:   jingnan
# Date:    2021/6/26
# Desc:

# http_request, post,get请求封装
import requests


class HttpRequest():

    def request(self, url, data, method, cookie=None):
        if method == 'get':
            res = requests.get(url, data, cookie)
        else:
            res = requests.post(url, data, cookie)
        return res


if __name__ == '__main__':
    url = 'http://localhost:8089/user/login.do'
    data = '{"username":"admin","password":"admin"}'
    httpRequest = HttpRequest()
    httpRequest.request(url, )