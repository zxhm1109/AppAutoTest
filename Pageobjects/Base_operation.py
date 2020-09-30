#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/24 16:31 
# @File      : Base_operation.py 
# @desc      :

from common.BasePage import BasePage
from appium.webdriver.common.mobileby import By

mall = (By.XPATH, '//androidx.appcompat.app.ActionBar.Tab[@content-desc="商城"]')
myhome = (By.XPATH, '//androidx.appcompat.app.ActionBar.Tab[@content-desc="我的"]')


class base_operation(BasePage):

    def base_Exist_page_text(self, text):
        """检查pageTitle是否为text"""
        self.sleep(1)
        loc = "//*[contains(@text,'{}')]".format(text)
        if self.driver.find_elements_by_xpath(loc):
            return True, (By.XPATH,loc)
        else:
            return False

    # def
