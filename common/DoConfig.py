#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:39 
# @File      : DoConfig.py 
# @desc      : 操作ini配置文件

import configparser
from common import path_conf
import logging as log


class RWConfig:

    @staticmethod
    def read_config(section, option):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='utf-8')
        # 根据标签、option获取值
        res = cf.get(section, option)
        return res

    @staticmethod
    def read_config_options_dict(section):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='utf-8')
        # 根据标签获取所有options
        options = cf.options(section)
        # 遍历获取value并放在dict
        config_dict = {}
        for option in options:
            config_dict[option] = cf.get(section, option)
        # rrr = cf.items(section)
        return config_dict

    @staticmethod
    def read_config_options_list(section):
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='utf-8')
        opt_list = cf.options(section)
        result = []
        for opt in opt_list:
            rrr = cf.get(section, opt)
            result.append(rrr)
        return result

    @staticmethod
    def write_config(section, option, value):
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='utf-8')
        cf.set(section, option, value)  # 修改指定section 的option
        with open(path_conf.Base_config_path, 'w') as f:
            cf.write(f)
        log.info('{} 更新成功'.format(section))


class rw_demo_conf:
    def r_demo(self, section):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='GBK')
        # 根据标签获取所有options
        options = cf.options(section)
        # 遍历获取value并放在dict
        config_dict = {}
        for option in options:
            config_dict[option] = cf.get(section, option)
        # rrr = cf.items(section)
        return config_dict

    def w_demo(self, section, option, value):
        if section == 'value' and option == 'uaa_1':
            value = 'GIF验证码图片'
        cf = configparser.ConfigParser()
        cf.read(path_conf.Base_config_path, encoding='GBK')
        cf.set(section, option, value)  # 修改指定section 的option
        with open(path_conf.Base_config_path, 'w') as f:
            cf.write(f)
        # log.info('{} 更新成功'.format(section))

    def get_demo_dict(self, tag):
        c = {}
        bb = ' '
        a = rw_demo_conf().r_demo('key')
        b = rw_demo_conf().r_demo('value')
        for x, y in a.items():
            for xx, yy in b.items():
                if x == xx:
                    c[y] = yy
        for ii, oo in c.items():
            if tag == ii:
                bb = oo
            else:
                pass
        return bb


if __name__ == '__main__':
    # WriteConfig.write_config('Base', 'Access_Token', '33asdasdsadsadsa33')
    a = RWConfig.read_config_options_dict('Android_options')
    print(a)
