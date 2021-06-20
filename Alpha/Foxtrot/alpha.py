# Author:   jingnan
# Date:    2021/6/20
# Desc: Python中的第三方包 http_request，以Gala Mall项目接口为例

import requests

# get请求,
url = 'http://localhost:8089/manage/category/get_category.do?categoryId=100001'
res = requests.get(url) # 返回消息实体  <Response [200]， 包含响应header，状态码，响应body

print(res)
print(res.headers)
print(res.status_code)
print(res.text)  # html，xml，json格式数据
