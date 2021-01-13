#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:49
# @File      : Run.py
# @desc      :

import sys
import platform
from common.BaseAndroidPhone import *
from common.BaseAdb import *
from common.pathUtils import pathUtils
# from common.BaseStatistics import countDate, writeExcel, countSumDevices
from Testcases import Test_live
from common.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
import multiprocessing
from datetime import datetime
from Testdatas.conf import Android_options
from Testdatas.conf import TestInterfaceCase
from selenium.common.exceptions import *


def runnerPool():
    """多设备测试"""
    devices = AndroidDebugBridge().get_devices()
    devices_Pool = []
    for _initApp in devices:
        suite = unittest.TestSuite()
        suite.addTest(TestInterfaceCase.parametrize(Test_live.Test_index, l_devices=_initApp))
        unittest.TextTestRunner(verbosity=2).run(suite)
    #     _pool = []
    #     _pool.append(_initApp)
    #     devices_Pool.append(_initApp)
    # pool = Pool(len(devices_Pool))
    # pool.map(runnerCaseApp, devices_Pool)
    # pool.close()
    # pool.join()


def runnerCaseApp():
    suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    suite.addTest(TestInterfaceCase.parametrize(Test_live.Test_index))
    # Test_live.Test_index().get_device(Android_options().get_android(devices))
    # suite.addTest(loader.loadTestsFromTestCase(Test_live.Test_index))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    # AppiumServer().start_appium_server(4723, 'NAB5T20506007667')
    try:
        runnerCaseApp()
    except WebDriverException as e:
        print('appium-service异常')
