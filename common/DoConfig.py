#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:39 
# @File      : DoConfig.py 
# @desc      : 操作ini配置文件

import configparser
from common.pathUtils import pathUtils
import logging as log


class RWConfig:

    def __init__(self):
        # 读取config文件
        self.cf = configparser.ConfigParser()
        self.cf.read(pathUtils().get_caseConfig_path(), encoding='utf-8')

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
        with open(pathUtils().get_caseConfig_path(), 'w') as f:
            cf.write(f)
        log.info('{} 更新成功'.format(section))


if __name__ == '__main__':
    RWConfig().write_config('Android_options', 'platformVersion', '33asdasdsadsadsa33')
    a = RWConfig().read_config_options_dict('Android_options')
    print(type(a))
