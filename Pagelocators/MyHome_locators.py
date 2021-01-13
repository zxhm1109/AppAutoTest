#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 14:00 
# @File      : MyHome_locators.py
# @desc      : 登录注册页面 及 免费变美专区页面

from appium.webdriver.common.mobileby import By as BY

"""个人中心"""

# """免费变美专区"""
# login_freeZone_phone = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/edt_phone")
# login_freeZone_send_verification_code = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/tv_get_code")
# login_freeZone_verification_code = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/edt_code")
# login_freeZone_invitation_code = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/edt_invite_code")
# login_freeZone_register = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/iv_register")
# login_freeZone_level = (BY.ID, "")  # 图片，无法验证
# login_freeZone_productlist = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/goods_recycler_view")
# login_freeZone_product = (BY.ID, "cn.sanshaoxingqiu.ssbm:id/iv_icon")
# login_freeZone_back = (BY.XPATH,
#                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")

# new 个人中心
login_start_confirm_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_ok')
login_myhome_ele = (BY.XPATH, '//android.widget.LinearLayout[@content-desc="我的"]')
myhome_avatar_ele = (BY.ID, "iv_avatar")
login_jump_ele = (BY.ID, "cn.sancell.ssbm:id/tv_jump")
myhome_order_ele = (BY.ID, "cn.sancell.ssbm:id/ll_all_order")
myhome_order_pay_ele = (BY.ID, "cn.sancell.ssbm:id/ll_order_tobepaid")
myhome_oder_usable_ele = (BY.ID, 'cn.sancell.ssbm:id/ll_order_tobeuse')
myhome_order_finish_ele = (BY.ID, 'cn.sancell.ssbm:id/ll_order_complete')
myhome_verify_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_identity')
myhome_referrer_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_my_referrer')
myhome_redpackage_balance_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_red_balance')
myhome_point_balance_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_conversion')
myhome_lottery_prize_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_my_prize')
myhome_myfans_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_my_fans')
myhome_invite_code_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_my_invite_code')
myhome_service_balance_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_income')
myhome_customer_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_phone')
customer_phone_ele = (BY.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView')
customer_link_ele = (BY.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView')
myhome_about_ele = (BY.ID, 'cn.sancell.ssbm:id/pav_aboutus')

# 退出登录
quit_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_logout')
quit_confirm_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_cancel')

# login 登录
login_user_ele = (BY.ID, 'cn.sancell.ssbm:id/edt_phone')
login_invite_ele = (BY.ID, 'cn.sancell.ssbm:id/edt_invite_code')
login_verify_ele = (BY.ID, 'cn.sancell.ssbm:id/edt_code')
login_get_verify_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_get_code')
login_checkBox_ele = (BY.ID, 'cn.sancell.ssbm:id/checkbox')
login_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_login')
login_agreement_plant_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_agreement')
login_agreement_policy_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_policy')

# has login
myhome_nickname_ele = (BY.XPATH,
                       '/0hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
myhome_isverify_ele = (BY.ID, 'cn.sancell.ssbm:id/rl_indetity')

# order 订单中心
order_all_ele = (BY.XPATH, '//android.widget.LinearLayout[@content-desc="全部"]')
order_pay_ele = (BY.XPATH, '//android.widget.LinearLayout[@content-desc="待支付"]')
order_usable_ele = (BY.XPATH, '//android.widget.LinearLayout[@content-desc="待使用"]')
order_finish_ele = (BY.XPATH, '//android.widget.LinearLayout[@content-desc="已完成"]')
oder_back_ele = (BY.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]')
order_list_status_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_state')
order_pay_but_ele = (BY.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView')

# live 创作中心
myhome_want_live_ele = (BY.ID, 'cn.sancell.ssbm:id/ll_live_live')
live_title_ele = (BY.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]')

# ident 主播申请
live_ident_Name_ele = (BY.ID, 'cn.sancell.ssbm:id/edt_name')
live_ident_CardId_ele = (BY.ID, 'cn.sancell.ssbm:id/edt_id')
live_ident_Card_photo1_ele = (BY.ID, 'cn.sancell.ssbm:id/fl_step_1')
live_ident_Card_photo2_ele = (BY.ID, 'cn.sancell.ssbm:id/ll_step_2')
live_ident_Card_photo3_ele = (BY.ID, 'cn.sancell.ssbm:id/fl_step_3')
live_ident_camera_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView')
live_ident_photo_ele = (BY.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView')
live_ident_root_ele = (BY.ID, 'com.android.permissioncontroller:id/permission_allow_button')

live_ident_fresh_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_cancel')

# 手机相册
phone_photo_album_ele = (BY.XPATH,
                         '//android.widget.ListView[@content-desc="本地相册"]/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]')
phone_photo_Image_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')
phone_photo_select_ele = (BY.XPATH, '//android.widget.ImageButton[@content-desc="确定"]')
# 手机拍照
phone_camera_preposition_ele = (BY.ID, 'com.huawei.camera:id/lyt_normal_control_bar_switcher_single')
phone_camera_take_ele = (BY.ID, 'com.huawei.camera:id/shutter_button')
phone_camera_select_ele = (BY.XPATH, '//android.widget.ImageView[@content-desc="确定"]')
live_ident_photo_loading_ele = (BY.ID, 'cn.sancell.ssbm:id/loading_text')
live_ident_submit_ele = (BY.ID, 'cn.sancell.ssbm:id/tv_submit')

# red_withdraw 红包提现
red_withdraw_invitation_ele = (BY.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]')
red_withdraw_balance_ele = (BY.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]')
red_withdraw_total_ele = (BY.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]')
red_withdrawing_price_ele = (BY.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[7]')

red_withdraw_ele = (BY.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]')
red_record_ele = (BY.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]')
red_withdraw_record_ele = (BY.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]')

# 银行卡列表
red_bankcard_list_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[4]')
red_bankcard_ele = (BY.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[18]/android.view.View[2]/android.view.View')
red_withdraw_input_ele = (BY.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[7]/android.view.View[2]/android.widget.EditText')
red_withdraw_accout_price_ele = (BY.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[9]')
red_withdraw_checkbox_ele = (BY.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.CheckBox/android.view.View[1]/android.view.View')
red_withdraw_submit_ele = (BY.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.Button')
red_withdraw_error_ele = (BY.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View')

red_withdraw_hint_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]')
