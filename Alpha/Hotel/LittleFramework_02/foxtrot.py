# Author:   jingnan
# Date:    2021/7/3
# Desc: 配置文件

# 以properties, config, ini, 结尾的为配置文件
#
import configparser


# 读取配置文件
# 创建一个对象
config = configparser.ConfigParser()
# 确定读取的文件
config.read('golf.config', encoding='utf-8')

# 读取数据方式一
res = config.get('CASE_IDS', 'case_ids')
print(res)

# 读取方式二
res_2 = config['CASE_IDS']['case_ids']
print(res_2)

# 读取sections
print(config.sections())

# 读取section中的键值对
print(config.items('CASE_IDS'))

# 数据类型,配置文件中的数据类型都是字符串，使用eval()将数据转化成原来的格式
print(type(config.get('MARVEL', 'name')))
print(type(config.get('MARVEL', 'num')))

