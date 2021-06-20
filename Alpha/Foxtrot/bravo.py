# Author:   jingnan
# Date:    2021/6/20
# Desc: 发送post请求，Gala Mall接口为例
import requests

url = 'http://localhost:8089/user/login.do'

# 默认是application/x-form-data
data = {'username': 'admin', 'password': 'admin'}
# 传application/json格式的数据使用 json = '{}'

res = requests.post(url, data)
print(res)

print(res.headers)
print(res.status_code)
print(res.text, type(res.text))  # 字符串类型
print(res.json(), type(res.json()))  # 字典类型
print(res.cookies) # cookie是类字典形式， key value形式
cookies = res.cookies
print(cookies['JSESSIONID']) # 取出cookie中的jsessionId
print(res.request.headers) # 获取请求头


# 接口返回格式是html， xml， json可以用text来接受
# 只有json格式返回值可以用json()接受

# 带cookie的get请求
# get请求,
url_2 = 'http://localhost:8089/manage/category/get_category.do?categoryId=100001'
res_2 = requests.get(url_2, cookies=cookies) # 返回消息实体  <Response [200]， 包含响应header，状态码，响应body
# 设置请求头
headers={'User-Agent':''}

print(res_2)
print(res_2.headers)
print(res_2.status_code)
print(res_2.text)  # html，xml，json格式数据