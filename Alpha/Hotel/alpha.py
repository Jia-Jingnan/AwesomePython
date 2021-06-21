# Author:   jingnan
# Date:    2021/6/21
# Desc:
from openpyxl import load_workbook


# 打开excel
bravo_workbook = load_workbook('bravo.xlsx')


# 指定操作的表单
sheet = bravo_workbook['test']


# 定位单元格， 根据行 列值定位
value = sheet.cell(1,1).value

print(value)

# 获取最大行
sheet.max_row
# 最大列
sheet.max_column

# 打印出行列值, 数据从excel中取出是什么类型？
# 数字还是数字，其他类型变为字符串类型
print("url：{}".format(sheet.cell(1,1).value, type(sheet.cell(1,1).value)))
print("data：{}".format(sheet.cell(1,2).value, type(sheet.cell(1,2).value)))
print("code：{}".format(sheet.cell(1,3).value, type(sheet.cell(1,3).value)))
print("method：{}".format(sheet.cell(1,4).value, type(sheet.cell(1,4).value)))