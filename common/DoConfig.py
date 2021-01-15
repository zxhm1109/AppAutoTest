#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:39 
# @File      : DoConfig.py 
# @desc      : 操作ini配置文件

import configparser
from common.pathUtils import pathUtils
from common.logger import Mylog
import yaml

log = Mylog('DoConfig.py ').getlog()


class RWConfig:

    def __init__(self):
        # 读取config文件
        self.cf = configparser.ConfigParser()
        self.cf.read(pathUtils().get_caseConfig_path(), encoding='utf-8-sig')

    def read_config(self, section, option):
        # 根据标签、option获取值
        res = self.cf.get(section, option)
        return res

    def read_config_options_dict(self, section):
        cf = self.cf
        # 根据标签获取所有options
        options = cf.options(section)
        # 遍历获取value并放在dict
        config_dict = {}
        for option in options:
            config_dict[option] = cf.get(section, option)
        # rrr = cf.items(section)
        return config_dict

    def read_config_options_list(self, section):
        cf = self.cf
        opt_list = cf.options(section)
        result = []
        for opt in opt_list:
            rrr = cf.get(section, opt)
            result.append(rrr)
        return result

    def write_config(self, section, option, value):
        cf = self.cf
        cf.set(section, option, value)  # 修改指定section 的option
        with open(pathUtils().get_caseConfig_path(), 'w', encoding='utf-8-sig') as f:
            cf.write(f)
        log.info('{} 更新成功'.format(section))


class yamlUtils:

    def __init__(self):
        self.yamlpath = pathUtils().get_yaml_path()

    def read(self, section=None, option=None):
        log.info('yaml中获取：{}中的{}'.format(section, option))
        with open(self.yamlpath, encoding='utf-8')as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        if section is None:
            return res
        else:
            if len(res) < 2:
                for sections, options in res.items():
                    if section not in sections:
                        return False, "未找到section"
                    elif option is None:
                        return res[section]
                    elif option not in options:
                        return False, "未找到option"
                    elif option in options:
                        return res[section][option]
            else:
                return res[section]

    def write(self, value, key=None):
        if isinstance(value, dict):
            for k, v in value.items():
                if self.read(k):
                    with open(self.yamlpath, 'a', encoding='utf-8')as f:
                        yaml.dump(value, f)
                        print("写入成功")
                else:
                    res = self.read()
                    res[k] = v
                    with open(self.yamlpath, 'a', encoding='utf-8')as f:
                        yaml.dump(res, f)
                    print("修改成功")
        else:
            if self.read(key):
                with open(self.yamlpath, 'a', encoding='utf-8')as f:
                    yaml.dump(value, f)
                print("修改成功")


if __name__ == '__main__':
    # a = RWConfig().read_config_options_dict('Android_options')
    # print(type(a))
    # yamlUtils().write(key='Tiktop',value=[{'1':'{1:2,3:5}'}])
    # RWConfig().write_config('TikTop', '8', str(data))
    # a = RWConfig().read_config_options_dict(section='TikTop')
    # print(a)
    ii = RWConfig().read_config_options_dict('TikTop')