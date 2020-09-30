#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 13:43 
# @File      : productList_page.py 
# @desc      :

from appium.webdriver.common.mobileby import By

productlist_back = (By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")
productlist_buy = (By.ID, "cn.sanshaoxingqiu.ssbm:id/btn_buy")
productlist_share = (By.ID, "cn.sanshaoxingqiu.ssbm:id/ll_share")
product_to_detail = (By.ID, "cn.sanshaoxingqiu.ssbm:id/tv_title")
productlist_share_wechat = (By.ID, "cn.sanshaoxingqiu.ssbm:id/recycler_view")
productlist_buttom = (By.ID, "cn.sanshaoxingqiu.ssbm:id/load_more_load_end_view")
productlist_buttom_text = (By.XPATH, "//*[contains(@text,'没有更多数据')]")
productlist_to_top = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_to_top")
