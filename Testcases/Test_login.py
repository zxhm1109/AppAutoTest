#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 16:25
# @File      : Test_login.py
# @desc      :

import unittest
from appium import webdriver
import time
from Pageobjects.index_page import IndexPage
from Pageobjects.productlist_page import ProductListPage
from Pageobjects.Base_operation import base_operation
from common.DoConfig import RWConfig


class Test_index(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "10"
        caps["deviceName"] = "P7C0218117013105"
        caps["appPackage"] = "cn.sanshaoxingqiu.ssbm"
        caps[
            "appActivity"] = "cn.sanshaoxingqiu.ssbm.module.splash.LaunchActivity"  #

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.base = base_operation(cls.driver)

    def setUp(self):
        time.sleep(3)

    def test_0_open_index(self):
        index = IndexPage(self.driver)
        # 划动首页并截图
        # index.index_swipe_screenshot()
        # 点击 跳至顶部 按钮
        # index.index_to_top()
        # 点击 第一个 专题 进入商品列表
        # index.index_open_product_list()
        backborp = index.index_backborp_num()
        self.assertEqual(backborp, 1)

        # index.index_swipe_banner()
        # self.assertFalse(self.base.base_Exist_page_text('三少变美'))

    # def test_1_check_productlist(self):
    #     plist = ProductListPage(self.driver)
    #     # plist.productlist_swipe_screenshot()
    #     # plist.productlist_to_top()
    #     plist.productlist_to_assign_product("【产后修复黄金套餐】（微针祛妊娠纹3次+蓝极光治疗3次）")
    #     self.assertFalse(base_operation(self.driver).base_Exist_page_text('商品列表'))


if __name__ == '__main__':
    unittest.main()
