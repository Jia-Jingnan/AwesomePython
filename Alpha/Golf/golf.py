# Author:   jingnan
# Date:    2021/6/21
# Desc:
import requests


class HttpRequest:

    def http_request(self,url,data,method,cookie=None):
        if method.lower() == 'get':
            res = requests.get(url,data,cookie)

        else:
            res = requests.post(url,data,cookie)

        return res



if __name__ == '__main__':
    pass