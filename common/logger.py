#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:55
# @File      : logger.py
# @desc      :

import logging
import time
from logging.handlers import RotatingFileHandler
from common import path_conf

fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datafmt = '%a, %d %b %Y %H:%M:%S'
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
handler_2 = RotatingFileHandler(path_conf.logs_path + '/APP_AutoTest_{}.log'.format(curTime), backupCount=20,
                                encoding='utf-8')
logging.basicConfig(format=fmt, datefmt=datafmt, level=logging.INFO, handlers=[handler_1, handler_2])
