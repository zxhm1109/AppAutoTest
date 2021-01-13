#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/10/20 10:45 
# @File      : conf.py 
# @desc      :
from common.logger import Mylog
import unittest


class Android_options:

    def __init__(self):
        self.logger = Mylog('conf.py').getlog()

    def get_android(self, devices):
        android = {'P7C0218117013105': {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "P7C0218117013105",
            "appPackage": "cn.sancell.ssbm",
            "appActivity": "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity"
            # ,"noReset": "true"  # 是否重置app
        }, 'huaweiP40': {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "NAB5T20506007667",
            "appPackage": "cn.sancell.ssbm",
            "appActivity": "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity"
            , "noReset": "true"
        }, 'd8bec445': {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "d8bec445",
            "appPackage": "cn.sancell.ssbm",
            "appActivity": "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity"
        }, 'samsungA9': {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "54c752a8",
            "appPackage": "cn.sancell.ssbm",
            "appActivity": "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity",
            "automationName": "UiAutomator1"
        }, 'vivox9': {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "ec2aaa0d",
            "appPackage": "cn.sancell.ssbm",
            "appActivity": "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity",
            "automationName": "UiAutomator1"
        }}
        caps = []
        cap = []

        if isinstance(devices, list):
            if devices:
                for device in devices:
                    for k, v in android.items():
                        if device == v['deviceName']:
                            caps.append(android[k])
                            cap.append(k)
                if cap:
                    self.logger.info('{}:设备未正常录入conf'.format(list(set(devices) ^ set(cap))))
                return caps
            else:
                self.logger.error('未正常连接设备')
        else:
            for k, v in android.items():
                for vv in v.values():
                    if devices == vv:
                        caps.append({k: android[k]})
            if not caps:
                self.logger.info('{}:设备未正常录入conf'.format(devices))
            self.logger.info('设备{} 检测正常'.format(caps[0]))
            return caps[0]


class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices
        # self.driver = ""


    @staticmethod
    def parametrize(testcase_klass):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name))
        return suite


if __name__ == '__main__':
    from common.BaseAdb import AndroidDebugBridge

    aa = AndroidDebugBridge().get_devices()

    a = Android_options().get_android(aa)
    print(a)
