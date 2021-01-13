#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 13:52 
# @File      : productlist_page.py 
# @desc      :

from Pagelocators import productList_locators as loc
from common.BasePage import BasePage
from Pageobjects.Base_operation import base_operation

doc = '商品列表'


class ProductListPage(BasePage):

    def product_list_buy(self):
        # 点击购买
        self.click_element(loc.productlist_buy)

    def product_list_share(self):
        # 分享至微信，暂不可用
        self.click_element(loc.productlist_share)
        self.click_element(loc.productlist_share_wechat)

    def product_list_productName(self):
        # 获取商品列表的 商品名称
        self.save_screenshot(doc)
        proName = self.get_elements(loc.product_to_detail)
        el = loc.product_to_detail[0].split(',')[-1]
        for Name in proName:
            loc1 = ('By.{}'.format(el), Name)
            print(loc1)
            self.get_text(loc1)

    def productlist_swipe_screenshot(self):
        # 滑动商品列表并截图
        num = 0
        while True:
            self.save_screenshot(doc)
            self.swipe_direction('up', 2)
            num += 1
            if self.is_eleExist(loc.productlist_buttom):
                self.save_screenshot(doc)
                break

    def productlist_to_top(self):
        # 点击返回至顶部
        self.click_element(loc.productlist_to_top)

    def productlist_to_assign_product(self, productName):
        # 点击进入指定商品详情
        while True:
            self.swipe_direction('up')
            if base_operation(self.driver).base_Exist_page_text(productName):
                x, y = base_operation(self.driver).base_Exist_page_text(productName)
                self.click_element(y)  # 点击进入productName 商品详情
                break
