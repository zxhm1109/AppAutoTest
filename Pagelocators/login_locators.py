#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 14:00 
# @File      : login_locators.py 
# @desc      : 登录注册页面 及 免费变美专区页面

from appium.webdriver.common.mobileby import By

"""免费变美专区"""
login_freeZone_phone = (By.ID, "cn.sanshaoxingqiu.ssbm:id/edt_phone")
login_freeZone_send_verification_code = (By.ID, "cn.sanshaoxingqiu.ssbm:id/tv_get_code")
login_freeZone_verification_code = (By.ID, "cn.sanshaoxingqiu.ssbm:id/edt_code")
login_freeZone_invitation_code = (By.ID, "cn.sanshaoxingqiu.ssbm:id/edt_invite_code")
login_freeZone_register = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_register")
login_freeZone_level = (By.ID, "")  # 图片，无法验证
login_freeZone_productlist = (By.ID, "cn.sanshaoxingqiu.ssbm:id/goods_recycler_view")
login_freeZone_product = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_icon")
login_freeZone_back = (By.XPATH,
                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")
