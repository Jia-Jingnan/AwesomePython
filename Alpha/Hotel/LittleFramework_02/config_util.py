# Author:   jingnan
# Date:    2021/7/3
# Desc: 配置文件读取类


import configparser

class ConfigUtil:

    def get_config(self,filename,section,option):
        config_obj = configparser.ConfigParser()
        config_obj.read(filename, encoding='utf-8')
        data = config_obj.get(section, option)
        return eval(data)


case_ids = ConfigUtil().get_config('golf.config', 'CASE_IDS', 'case_ids')
print(case_ids)

