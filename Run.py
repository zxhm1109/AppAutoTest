#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:49
# @File      : Run.py
# @desc      :
from random import random
import sys

from paramunittest import ParametrizedTestCase

sys.path.append("..")
import platform
from common.BaseAndroidPhone import *
from common.BaseAdb import *
# from common.BaseStatistics import countDate, writeExcel, countSumDevices
from Testcases import Test_login
from common.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")

    # def runnerPool(getDevices):
    """多设备测试"""


#     devices_Pool = []
#
#     for i in range(0, len(getDevices)):
#         _pool = []
#         _initApp = {}
#         _initApp["deviceName"] = getDevices[i]["devices"]
#         _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
#         _initApp["platformName"] = "android"
#         _initApp["port"] = getDevices[i]["port"]
#         _initApp["automationName"] = "uiautomator2"
#         _initApp["systemPort"] = getDevices[i]["systemPort"]
#
#         _initApp["app"] = getDevices[i]["app"]
#         _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
#         _initApp["appActivity"] = apkInfo.getApkActivity()
#         _pool.append(_initApp)
#         devices_Pool.append(_initApp)
#
#     pool = Pool(len(devices_Pool))
#     pool.map(runnerCaseApp, devices_Pool)
#     pool.close()
#     pool.join()


def runnerCaseApp():
    starttime = datetime.now()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_login.Test_index))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    # countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")


# if __name__ == '__main__':
#
#     # kill_adb()
#
#     devicess = AndroidDebugBridge().attached_devices()
#     if len(devicess) > 0:
#         mk_file()
#         l_devices = []
#         for dev in devicess:
#             app = {}
#             app["devices"] = dev
#             init(dev)
#             app["port"] = str(random.randint(4700, 4900))
#             app["bport"] = str(random.randint(4700, 4900))
#             app["systemPort"] = str(random.randint(4700, 4900))
#             app["app"] = PATH("/APK/")  # 测试的app路径
#
#             l_devices.append(app)
#
#         appium_server = AppiumServer(l_devices)
#         appium_server.start_server()
#         runnerPool(l_devices)
#         writeExcel()
#         appium_server.stop_server(l_devices)
#     else:
#         print("没有可用的安卓设备")

if __name__ == '__main__':
    runnerCaseApp()
