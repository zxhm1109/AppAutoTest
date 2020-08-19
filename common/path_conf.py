#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:54
# @File      : path_conf.py
# @desc      :

import os

base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

logs_path = os.path.join(base_path, 'Outputs/logs')
config_path = os.path.join(base_path, '')
screenShot_path = os.path.join(base_path, 'Outputs/ScreenShot')

if __name__ == '__main__':
    print(base_path)

