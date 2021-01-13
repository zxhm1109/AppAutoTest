#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/20 18:39 
# @File      : baseAndroidPhone.py 
# @desc      : 获取安卓手机设备信息


import os
import subprocess
import logging
from appium import webdriver
from common.BaseAdb import AndroidDebugBridge



def getPhoneInfo(devices):
    """获取手机基本信息"""
    cmd = "adb -s " + devices + " shell cat /system/build.prop "
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result = {"release": "5.0", "model": "model2", "brand": "brand1", "device": "device1"}
    release = "ro.build.version.release="  # 版本
    model = "ro.product.model="  # 型号
    brand = "ro.product.brand="  # 品牌
    device = "ro.product.device="  # 设备名
    for line in phone_info:
        for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device):]
                break
    logging.info("测试设备信息：{}".format(result))
    return result


def get_men_total(devices):
    """获取设备运行内存"""
    cmd = "adb -s " + devices + " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) + 1:].replace("kB", "").strip()
            break
    return int(men_total)


def get_cpu_kel(devices):
    """获取设备CPU信息"""
    cmd = "adb -s " + devices + " shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"


def get_app_pix(devices):
    """获取设备分辨率"""
    result = os.popen("adb -s " + devices + " shell wm size", "r")
    return result.readline().split("Physical size:")[1]


def start_device():
    # 启动android服务
    platformVersion = AndroidDebugBridge().get_android_version()
    # devicename = AndroidDebugBridge().get_devices()[0]
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = platformVersion
    caps["deviceName"] = "d8bec445"
    caps["appPackage"] = "cn.sancell.ssbm"
    caps["appActivity"] = "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    return driver


if __name__ == "__main__":
    getPhoneInfo("P7C0218117013105")
