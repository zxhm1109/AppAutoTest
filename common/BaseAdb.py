#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/20 18:27
# @File      : BaseAdb.py
# @desc      : adb 操作封装


import subprocess
import os
from common.logger import Mylog


class AndroidDebugBridge(object):

    def __init__(self):
        self.logger = Mylog('BaseAdb.py').getlog()

    # adb 命令封装
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # 检查设备devices
    def get_devices(self):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()
        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
            if 'offline' in t[0]:
                self.logger.info('{}设备未正常连接'.format(t[0].split('\t')[0]))
        return devices

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def android_reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def copy_file(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 打开指定app
    def open_app(self, packagename, activity):
        result = self.call_adb("shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 获取设备android版本
    def get_android_version(self):
        result = self.call_adb("shell getprop 'ro.build.version.release'")
        return result

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep " + pkg_name)
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]

    def run_monkey(self, nmb):
        with open("../Testdatas/android_locat.txt", 'a')as f:
            pass
        monkey_command = r"adb shell monkey -p cn.sancell.ssbm -v -v -v --throttle 500 --pct-touch 60 %s >C:\Users\ai013\Desktop\locat.txt" % nmb
        subprocess.Popen(monkey_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()


if __name__ == '__main__':
    a = AndroidDebugBridge().get_devices()
    print(a)
