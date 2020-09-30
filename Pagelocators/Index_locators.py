#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:10 
# @File      : Index_locators.py 
# @desc      : 首页元素集合

from appium.webdriver.common.mobileby import By

index_banner = (By.ID, "cn.sanshaoxingqiu.ssbm:id/banner_image")
index_img_advertisement = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_ad")
index_backborp_to_ProductList = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_bg")
index_to_productList = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_content")
index_product = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_icon")
index_to_top = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_to_top")
index_bottom = (By.ID, "cn.sanshaoxingqiu.ssbm:id/ll_bottom_line")
index_bottom_text = (By.XPATH,"//*[contains(@text,'已经到底啦')]")
index_banner_botton=(By.ID,"cn.sanshaoxingqiu.ssbm:id/ll_view")