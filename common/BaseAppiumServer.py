#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:59 
# @File      : BaseAppiumServer.py 
# @desc      : 启动appium


import os
import socket
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import time
import platform
import subprocess

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import threading


class AppiumServer:
    def __init__(self, kwargs=None):
        self.kwargs = kwargs

    # def start_server(self):
    #     """启动服务
    #     """
    #     for i in range(0, len(self.kwargs)):
    #         cmd = "appium --session-override  -p %s -bp %s -U %s" % (
    #             self.kwargs[i]["port"], self.kwargs[i]["bport"], self.kwargs[i]["devices"])
    #         print(cmd)
    #         if platform.system() == "Windows":  # windows下启动server
    #             t1 = RunServer(cmd)
    #             p = Process(target=t1.start())
    #             p.start()
    #             while True:
    #                 print("--------start_win_server-------------")
    #                 if self.win_is_runnnig("http://127.0.0.1:" + self.kwargs[i]["port"] + "/wd/hub" + "/status"):
    #                     print("-------win_server_ 成功--------------")
    #                     break
    #         else:
    #             appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
    #                                       close_fds=True)
    #             while True:
    #                 appium_line = appium.stdout.readline().strip().decode()
    #                 time.sleep(1)
    #                 print("---------start_server----------")
    #                 if 'listener started' in appium_line or 'Error: listen' in appium_line:
    #                     print("----server_ 成功---")
    #                     break

    def win_is_runnnig(self, url):
        """检查服务运行情况
        :return:True or False
        """
        response = None
        time.sleep(1)
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        except socket.timeout:
            return False
        finally:
            if response:
                response.close()

    def stop_server(self, devices):
        sysstr = platform.system()

        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                # mac
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plisttmp = plist[1].split("    ")
                plists = plisttmp[1].split(" ")
                # print plists[0]
                os.popen("kill -9 {0}".format(plists[0]))

    # def re_start_server(self):
    #     """重启服务
    #     """
    #     self.stop_server()
    #     self.start_server()

    def start_appium(self):
        '''node 与appium版本不匹配，启动服务有问题'''
        appium_path = r'cd C:\Program Files\Appium\resources\app\node_modules\appium\build\lib'
        start_appium = 'node main.js'
        subprocess.Popen(appium_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        subprocess.Popen(start_appium, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        if self.win_is_runnnig("http://127.0.0.1:" + '4723' + "/wd/hub" + "/status"):
            print("-------win_server_ Fail--------------")
        else:
            print("-------win_server_ SUCCEED--------------")

    def start_appium_server(self, port, devices):
        bootstrip = port + 1
        os.system("appium -a 127.0.0.1" + " -p " + str(port) + " -bp " + str(bootstrip) + " -U " + str(devices) + " --no-reset")

    class RunServer(threading.Thread):
        def __init__(self, cmd):
            threading.Thread.__init__(self)
            self.cmd = cmd

        def run(self):
            os.system(self.cmd)


if __name__ == '__main__':
    AppiumServer().start_appium()
