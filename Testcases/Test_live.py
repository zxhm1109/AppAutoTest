#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/12/17 15:35 
# @File      : Test_live.py 
# @desc      :

import unittest
from common.dbUtils import PostgreConn
import time
from Pageobjects import Live_page, Base_operation
from Testdatas.conf import *
from Pageobjects import MyHome_page, MallMedicine_page
from appium import webdriver
from common.logger import Mylog
from common import BaseAndroidPhone
from ddt import data, ddt
from selenium.common.exceptions import *
from Testdatas import sqlUtils as sql

logger = Mylog('Test_live.py').getlog()


class Test_index(TestInterfaceCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.l_devices = 'NAB5T20506007667'
        # super(Test_index, self).setUp()
        caps = Android_options().get_android(cls.l_devices)
        cls.phone = list(caps.keys())[0]
        cls.cap = list(caps.values())[0]
        logger.info('开始启动设备-------->>>>,{}'.format(cls.phone))
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cls.cap)
        cls.myhomeP = MyHome_page.LoginPage(cls.driver)
        cls.baseP = Base_operation.base_operation(cls.driver)
        cls.mallP = MallMedicine_page.IndexPage(cls.driver)
        cls.baseP.start_app_confirm()


    def setUp(self):
        # super(Test_index, self).setUp()
        # self.phone = list(Android_options().get_android(self.l_devices).keys())[0]
        # self.cap = list(Android_options().get_android(self.l_devices).values())[0]
        # print('开始启动设备-------->>>>,{}'.format(self.phone))
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.cap)
        # time.sleep(2)
        # self.myhomeP = MyHome_page.LoginPage(self.driver)
        # self.baseP = Base_operation.base_operation(self.driver)
        # self.mallP = MallMedicine_page.IndexPage(self.driver)
        # self.baseP.start_app_confirm()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.baseP.To_app_index()
        self.baseP.sleep(1)

    def test_10_nologin_myhome(self):
        """
        未登录时个人中心菜单入口点击跳转登录页面
        """
        self.myhomeP.to_login()
        self.baseP.back(2)
        self.myhomeP.Myhome_login_check('个人中心未登录时菜单点击验证')

    def test_11_login(self):
        """不勾选协议时登录"""
        self.myhomeP.to_login()
        self.myhomeP.login()
        self.myhomeP.click_check_box()
        self.myhomeP.click_login()
        self.assertFalse(self.myhomeP.check_islogin())

    def test_20_login(self):
        """正常登录"""
        self.myhomeP.to_login()
        self.myhomeP.login('13120806671')
        self.myhomeP.click_login()
        self.assertTrue(self.myhomeP.check_islogin())

    def test_30_order_status(self):
        """购买商品流程"""
        self.baseP.To_mall_medicine()
        # 商品列表
        # self.mallp.mall_index_find_subject()
        self.mallP.mall_buy_product()

    def test_40_order_detail(self):
        """登录后，检查待支付订单详情信息"""
        self.baseP.To_myhome()
        self.myhomeP.to_login()
        self.myhomeP.login('13120806671')
        self.myhomeP.click_login()
        self.myhomeP.check_order_list('待支付')
        self.myhomeP.order_pay()
        self.mallP.paytype_alipay()
        self.mallP.alipay()
        self.baseP.back(3)

    # def test_50_mall_shopping(self):
    #
    # # """登录后，订单列表状态是否正常"""
    # #     self.assertTrue(self.myhomeP.check_order_list('待支付'), '待支付')
    # #     self.myhomeP.order_back()
    # #     self.assertTrue(self.myhomeP.check_order_list('待使用'), '待使用')
    # #     self.myhomeP.order_back()
    # #     self.assertTrue(self.myhomeP.check_order_list('已完成'), '已完成')
    # #     self.myhomeP.order_back()

    def test_60_live_ident(self):
        """主播身份认证"""
        # 重置主播认证状态
        PostgreConn().UpdataOperate(sql.updata_User_audit_status)

        self.baseP.To_myhome()
        self.myhomeP.to_login()
        self.myhomeP.login('16666666663')
        self.myhomeP.click_login()
        self.myhomeP.live_ident_anchor()
        User_audit_status = PostgreConn().SelectOperate(sql.select_User_audit_status)
        self.assertTrue('SUCCESS', User_audit_status)

    def test_70_redpackage_withdraw(self):
        """红包余额，提现，记录"""
        PostgreConn().UpdataOperate(sql.updata_User_withdraw_record)
        self.baseP.To_myhome()
        self.myhomeP.to_login()
        self.myhomeP.login('13120806671')
        self.myhomeP.click_login()
        self.myhomeP.to_red_withdraw()
        self.myhomeP.red_withdraw()
        self.assertTrue(self.myhomeP.check_success_msg(), True)


if __name__ == '__main__':
    try:
        unittest.main()
    except WebDriverException as e:
        unittest.main()
