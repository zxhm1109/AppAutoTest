#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/24 16:31 
# @File      : Base_operation.py 
# @desc      :

from common.BasePage import BasePage
from appium.webdriver.common.mobileby import By
from docopt import docopt
from common.logger import Mylog

medicine_mall_menu = (By.XPATH, '//android.widget.LinearLayout[@content-desc="医美商城"]')
myhome_menu = (By.XPATH, '//android.widget.LinearLayout[@content-desc="我的"]')
live_menu = (By.XPATH, '//android.widget.LinearLayout[@content-desc="直播"]')
IPmall_menu = (By.XPATH, '//android.widget.LinearLayout[@content-desc="IP商城"]')

login_start_confirm_ele = (By.ID, 'cn.sancell.ssbm:id/tv_ok')

ranking_ele = (By.ID, 'cn.sancell.ssbm:id/iv_ranking')

quit_ele = (By.ID, 'cn.sancell.ssbm:id/tv_logout')


# logger = Mylog('Base_operation.py').getlog()


class base_operation(BasePage):

    def base_Exist_page_text(self, text):
        """检查pageTitle是否为text"""
        self.sleep(1)
        loc = "//*[contains(@text,'{}')]".format(text)
        if self.driver.find_elements_by_xpath(loc):
            return True, (By.XPATH, loc)
        else:
            return False

    def start_app_confirm(self):
        """启动页点击确定按钮"""
        if self.is_eleExist(login_start_confirm_ele):
            self.click_element(login_start_confirm_ele)

    @staticmethod
    def get_doc():
        """1111"""
        arguments = docopt(__doc__)
        print(arguments)
        return arguments

    def to_ranking(self):
        self.click_element(ranking_ele)

    def To_mall_medicine(self):
        self.click_element(medicine_mall_menu)

    def To_myhome(self):
        self.click_element(myhome_menu)

    def To_mall_IP(self):
        self.click_element(IPmall_menu)

    def To_live(self):
        self.click_element(live_menu)

    def quit(self):
        self.swipe_find_ele(quit_ele, 'c', 'up')

    def To_app_index(self):
        num = 5
        while num:
            if self.is_eleExist(myhome_menu):
                self.To_live()
                break
            else:
                self.back()
                num -= 1
