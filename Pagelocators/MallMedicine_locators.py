#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 11:10 
# @File      : MallMedicine_locators.py
# @desc      : 首页元素集合

from appium.webdriver.common.mobileby import By

"""医美商城"""

index_banner = (By.ID, "cn.sanshaoxingqiu.ssbm:id/banner_image")
index_img_advertisement = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_ad")
index_backborp_to_ProductList = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_bg")
index_to_productList = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_content")
index_product = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_icon")
index_to_top = (By.ID, "cn.sanshaoxingqiu.ssbm:id/iv_to_top")
index_bottom = (By.ID, "cn.sanshaoxingqiu.ssbm:id/ll_bottom_line")
index_bottom_text = (By.XPATH, "//*[contains(@text,'已经到底啦')]")
index_banner_botton = (By.ID, "cn.sanshaoxingqiu.ssbm:id/ll_view")
index_subject_text = (By.XPATH, '//*[contains(@text,"测试不要删除90")]')

index_mall_menu_ele = (By.XPATH, '乔丽尔医美旗舰店热卖商品')

# 商品详情
detail_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_price')
detail_goodsName_ele = (By.ID, 'cn.sancell.ssbm:id/tv_goods_name')
detail_sellNum_ele = (By.ID, 'cn.sancell.ssbm:id/tv_sell_num')
detail_explain_ele = (By.ID, 'cn.sancell.ssbm:id/ll_introduction')
detail_recommend_ele = (By.ID, "cn.sancell.ssbm:id/iv_recommend_reward")
detail_hospital_Name_ele = (By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
detail_hospital_addres_ele = (By.ID, 'cn.sancell.ssbm:id/tv_address')
detail_hospital_phone_ele = (By.ID, 'cn.sancell.ssbm:id/iv_call_phone')
detail_consult_ele = (By.ID, 'cn.sancell.ssbm:id/ll_consult')
detail_share_ele = (By.ID, 'cn.sancell.ssbm:id/ll_share')

detail_buy_ele = (By.ID, "cn.sancell.ssbm:id/btn_buy")

# confirm 确认订单
confirm_hospital_phone_ele = (By.ID, 'cn.sancell.ssbm:id/tv_tel')
confirm_hospital_worktime_ele = (By.ID, 'cn.sancell.ssbm:id/tv_time')
confirm_hospital_addres_ele = (By.ID, 'cn.sancell.ssbm:id/tv_address')

confirm_hospital_Name_ele = (By.ID, 'cn.sancell.ssbm:id/ll_title_bg')
confirm_productName_ele = (By.ID, 'cn.sancell.ssbm:id/tv_title')
confirm_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_price')

confirm_product_minus_ele = (By.ID, 'cn.sancell.ssbm:id/rl_minus')
# 联动共计商品
confirm_product_num1_ele = (By.ID, 'cn.sancell.ssbm:id/tv_buy_count')
# 共计商品
confirm_product_num2_ele = (By.ID, 'cn.sancell.ssbm:id/tv_buy_num1')
# 底部共计商品
confirm_product_num3_ele = (By.ID, 'cn.sancell.ssbm:id/tv_buy_num2')
confirm_product_plus_ele = (By.ID, 'cn.sancell.ssbm:id/rl_plus')

confirm_remark_ele = (By.ID, 'cn.sancell.ssbm:id/edt_remark')
confirm_total_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_total_price1')
# 底部合计
confirm_total2_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_total_price3')

confirm_pay_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_total_price2')
confirm_User_nickname_ele = (By.ID, 'cn.sancell.ssbm:id/tv_nick_name')
confirm_User_phone_ele = (By.ID, 'cn.sancell.ssbm:id/tv_nick_name')

confirm_checkbox_ele = (By.ID, 'cn.sancell.ssbm:id/checkbox')

confirm_order_ele = (By.ID, 'cn.sancell.ssbm:id/btn_confirm')

# payment 确认付款
payment_orderId_ele = (By.ID, 'cn.sancell.ssbm:id/tv_order_no')  # 订单编号：
payment_total_price_ele = (By.ID, 'cn.sancell.ssbm:id/tv_price')  # ¥
payment_wechatpay_ele = (By.ID, 'cn.sancell.ssbm:id/ll_pay_wechat')
payment_alipay_ele = (By.ID, 'cn.sancell.ssbm:id/check_alipay')

payment_start_pay_ele = (By.ID, 'cn.sancell.ssbm:id/btn_start_pay')

# 打开支付宝
payment_open_alipay_ele = (By.ID, 'android:id/button1')
# 支付宝支付
payment_alipay_pay_ele = (By.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]')


def loc_contains_text(text):
    """"补充xpath，模糊文本定位模板"""
    ele = (By.XPATH, '//*[contains(@text,"{}")]'.format(text))
    return ele
