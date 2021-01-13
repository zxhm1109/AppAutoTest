#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:46
# @File      : MallMedicine_page.py
# @desc      :

from common.BasePage import BasePage
from Pagelocators import MallMedicine_locators as loc
from common.logger import Mylog


class IndexPage(BasePage):
    doc = '医美商品首页'
    logger = Mylog('MallMedicine_page.py').getlog()

    def index_swipe_banner(self):
        # 划动banner 未定位
        self.swipe_direction('left', 10)

    def index_to_banner(self):
        self.click_element(loc.index_banner)

    def index_to_product(self):
        self.swipe_direction('up', 2)
        self.click_element(locator=loc.index_product, doc=self.doc)  # 点击去详情

    def index_open_product_list(self):
        self.swipe_direction('up', 9)
        self.get_element(locator=loc.index_to_productList, doc=self.doc).click()

    def index_to_top(self):
        self.click_element(loc.index_to_top)

    def index_swipe_screenshot(self):
        """滑动首页至底部，并截图"""
        num = 1
        while True:
            self.logger.info("第{}划动截图".format(num))
            self.save_screenshot('index_' + str(num))
            self.swipe_direction('up', 2)
            num += 1
            if self.is_eleExist(loc.index_bottom_text):
                self.save_screenshot('index_' + str(num))
                break

    def mall_index_find_subject(self):
        self.swipe_find_ele(loc.index_subject_text, 'c', 'up')

    def mall_index_find_product(self, str):
        self.swipe_find_ele(loc.loc_contains_text(str), 'c', 'up')

    def index_backborp_num(self):
        # 获取有背景专题list（计算个数）
        return len(self.get_elements(loc.index_backborp_to_ProductList))

    def check_product_details(self):
        self.get_text()

    def mall_buy_product(self):
        self.mall_index_find_product('jmeter测试商品1')

        self.click_element(loc.detail_buy_ele)
        self.click_element(loc.confirm_order_ele)
        self.paytype_alipay()
        self.alipay()

    def paytype_alipay(self):
        self.click_element(loc.payment_alipay_ele)
        self.click_element(loc.payment_start_pay_ele)

    def alipay(self):
        if self.is_eleExist(loc.payment_open_alipay_ele):
            self.click_element(loc.payment_open_alipay_ele)
        self.sleep(2)
        self.click_element(loc.payment_alipay_pay_ele)
        self.sleep(1)
        self.click_tap([222, 1733])
        self.sleep(1)
        self.click_tap([222, 1733])
        self.sleep(1)
        self.click_tap([550, 2250])
        self.sleep(1)
        self.click_tap([222, 1733])
        self.sleep(1)
        self.click_tap([600, 1733])
        self.sleep(1)
        self.click_tap([550, 2250])
