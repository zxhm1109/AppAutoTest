#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:46
# @File      : __init__.py.py
# @desc      :

from common.BasePage import BasePage
from Pagelocators import Index_locators as loc
import logging as logger


class IndexPage(BasePage):
    doc = '首页'

    def index_swipe_banner(self):
        # 划动banner 未定位
        self.swipe_direction('left', 10)

    def index_to_product(self):
        self.swipe_direction('up', 2)
        self.click_element(locator=loc.index_product, doc=self.doc)  # 点击去详情

    def index_open_product_list(self):
        self.swipe_direction('up', 9)
        self.get_element(locator=loc.index_to_productList, doc=self.doc).click()

    def index_to_top(self):
        self.click_element(loc.index_to_top)

    def index_to_banner(self):
        self.click_element(loc.index_banner)

    def index_swipe_screenshot(self):
        """滑动首页至底部，并截图"""
        num = 1
        while True:
            logger.info("第{}划动截图".format(num))
            self.save_screenshot('index_' + str(num))
            self.swipe_direction('up', 2)
            num += 1
            if self.eleExist(loc.index_bottom_text):
                self.save_screenshot('index_' + str(num))
                break

    def index_backborp_num(self):
        # 获取有背景专题list（计算个数）
        return len(self.get_elements(loc.index_backborp_to_ProductList))
