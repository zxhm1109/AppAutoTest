#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:54
# @File      : pathUtils.py
# @desc      :

import os
import time


class pathUtils:
    def __init__(self):
        # 项目路径
        self.project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_case_path(self):
        # 用例文件路径
        case_path = os.path.join(self.project_path, 'Testdatas', '')
        return case_path

    def get_case_py_path(self):
        # 测试用例代码路径
        case_path = os.path.join(self.project_path, 'test_case')
        return case_path

    def get_report_html_path(self):
        # html测试报告路径
        if not os.path.exists(os.path.join(self.project_path, 'Outputs', 'report')):
            os.makedirs(os.path.join(self.project_path, 'Outputs', 'report'))
        html_report_path = os.path.join(self.project_path, 'Outputs', 'report',
                                        str(time.strftime('%Y%m%d',
                                                          time.localtime())) + '_test_app_report.html')
        return html_report_path

    def get_caseConfig_path(self):
        # conf配置文件路径
        caseConfig_path = os.path.join(self.project_path, 'Testdatas',
                                       'BaseConfig.ini')
        return caseConfig_path

    def get_log_path(self):
        # 日志文件路径
        log_path = os.path.join(self.project_path, 'Outputs', 'logs',
                                str(time.strftime('%Y%m%d', time.localtime())) + '_AppTest.log')
        return log_path

    def get_yaml_path(self):
        # yaml配置文件路径
        yaml_path = os.path.join(self.project_path, 'Testdatas', 'Deployer.yaml')
        return yaml_path

    def get_screenShot_path(self, doc):
        # 截图保存路径
        if not os.path.exists(os.path.join(self.project_path, 'Outputs', 'ScreenShot')):
            os.makedirs(os.path.join(self.project_path, 'Outputs', 'ScreenShot'))
        path = os.path.join(self.project_path, 'Outputs', 'ScreenShot', str('{}_{}.png'.format(doc, time.strftime('%Y-%m-%d-%H-%M-%S',
                                                                                                                  time.localtime()))))
        return path


if __name__ == '__main__':
    import time

    # print(os.path.join(os.path.split(os.getcwd())[0],'log',str(time.strftime('%Y%m%d',time.localtime()))+'_ApiTest.log'))
    # a=file_path().get_caseConfig_path()
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_PATH)
    print(pathUtils().project_path)
    # print(type(time.strftime('%Y%m%d',time.localtime())))
