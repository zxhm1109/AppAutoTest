#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 14:00 
# @File      : MyHome_page.py
# @desc      : 登录页面 及 免费变美专区

from Pagelocators import MyHome_locators as loc
from common.BasePage import BasePage
from common.logger import Mylog

logger = Mylog("MyHome_page.py").getlog()


class LoginPage(BasePage):

    def jump_check(self, locs, doc=''):
        self.click_element(locs, doc)
        self.click_element(loc.login_jump_ele, doc)

    def Myhome_login_check(self, doc=''):
        """未登录时遍历个人中心菜单验证登录状态"""
        self.wait(10)
        self.swipe_direction('down', 3, 9)
        self.jump_check(loc.myhome_avatar_ele, doc)
        self.jump_check(loc.myhome_order_ele, doc)
        self.jump_check(loc.myhome_order_pay_ele, doc)
        self.jump_check(loc.myhome_order_finish_ele, doc)
        self.jump_check(loc.myhome_want_live_ele, doc)
        self.jump_check(loc.myhome_verify_ele, doc)
        self.swipe_direction('up', 1, 4)
        self.jump_check(loc.myhome_referrer_ele, doc)
        self.jump_check(loc.myhome_redpackage_balance_ele, doc)
        # 兑换奖励展示奖励金，无法点击
        # self.swipe_direction('up', 1, 500)
        self.click_element(loc.myhome_point_balance_ele, doc)
        self.swipe_direction('up', 1, 4)
        self.jump_check(loc.myhome_lottery_prize_ele, doc)
        # self.swipe_direction('up', 1, 2500)
        self.jump_check(loc.myhome_myfans_ele, doc)
        self.jump_check(loc.myhome_invite_code_ele, doc)
        # 点击联系客服弹窗选择 电话/在线客服
        self.swipe_direction('up', 1, 4)
        self.click_element(loc.myhome_customer_ele, doc)
        self.click_element(loc.customer_phone_ele, doc)
        self.back(2)
        self.click_element(loc.myhome_customer_ele, doc)
        self.jump_check(loc.customer_link_ele, doc)

    def login(self, user='16666666663', password='8888', invite='', doc='登录'):
        """登录"""
        self.input_text(loc.login_user_ele, user, doc)
        self.click_element(loc.login_get_verify_ele, doc)
        self.input_text(loc.login_verify_ele, password, doc)
        self.input_text(loc.login_invite_ele, invite, doc)

    def click_check_box(self):
        self.click_element(loc.login_checkBox_ele)

    def click_login(self):
        self.click_element(loc.login_ele)

    def to_login(self):
        self.click_element(loc.login_myhome_ele)
        if self.to_about():
            return True
        else:
            self.click_element(loc.quit_ele)
            self.click_element(loc.quit_confirm_ele)
            self.sleep(1)

    def check_nickname_exist(self):
        return self.is_eleExist(loc.myhome_nickname_ele)

    def check_islogin(self):
        self.swipe_direction('down', 3)
        return self.is_eleExist(loc.myhome_isverify_ele)

    def check_order_list(self, status):
        self.swipe_direction('down', 3)
        self.swipe_find_ele(loc.myhome_order_ele, 'c', 'up')
        self.click_element(loc.order_pay_ele)
        self.click_element(loc.order_usable_ele)
        self.click_element(loc.order_finish_ele)
        self.click_element(loc.order_all_ele)
        if status.lower() == "待支付":
            self.click_element(loc.order_pay_ele)
            return self.get_elements_text(loc.order_list_status_ele)
        elif status.lower() == "待使用":
            self.click_element(loc.order_usable_ele)
            return self.get_elements_text(loc.order_list_status_ele)
        elif status.lower() == "已完成":
            self.click_element(loc.order_finish_ele)
            return self.get_elements_text(loc.order_list_status_ele)

    def order_pay(self):
        """跳转至确认付款"""
        self.click_element(loc.order_pay_but_ele)

    def order_back(self):
        self.click_element(loc.oder_back_ele)

    def live_ident_anchor(self):
        """主播身份认证"""
        self.swipe_direction('down', 3)
        self.swipe_find_ele(loc.myhome_want_live_ele, 'down')
        if self.is_eleExist(loc.live_ident_fresh_ele):
            self.click_element(loc.live_ident_fresh_ele)
            self.sleep(1)
        self.input_text(loc.live_ident_Name_ele, '测试主播2021')
        self.input_text(loc.live_ident_CardId_ele, '411502199111148728')
        self.click_element(loc.live_ident_Card_photo1_ele)
        self.huawei_photo_select('c')
        self.click_element(loc.live_ident_Card_photo2_ele)
        self.huawei_photo_select('p')
        self.click_element(loc.live_ident_Card_photo3_ele)
        self.huawei_photo_select('p')
        self.sleep(3)
        self.click_element(loc.live_ident_submit_ele)

    def huawei_photo_select(self, action='c'):
        """图片上传"""
        num = 3
        while num:
            if not self.is_eleExist(loc.live_ident_photo_loading_ele):
                if action == 'p':
                    self.click_element(loc.live_ident_photo_ele)
                    if self.is_eleExist(loc.live_ident_root_ele):
                        self.click_element(loc.live_ident_root_ele)

                    # 选择相册
                    self.click_element(loc.phone_photo_album_ele)
                    # 选择照片
                    self.click_element(loc.phone_photo_Image_ele)
                    # 确认照片
                    self.click_element(loc.phone_photo_select_ele)
                    break
                if action == 'c':
                    self.click_element(loc.live_ident_camera_ele)
                    # 权限确认
                    if self.is_eleExist(loc.live_ident_root_ele):
                        self.click_element(loc.live_ident_root_ele)
                    # 翻转摄像头
                    self.click_element(loc.phone_camera_preposition_ele)
                    # 拍照
                    self.click_element(loc.phone_camera_take_ele)
                    # 确认照片
                    self.click_element(loc.phone_camera_select_ele)
                    break
            else:
                num -= 1

    def to_live(self):
        self.click_element(loc.myhome_want_live_ele)

    def to_red_withdraw(self):
        self.click_element(loc.myhome_redpackage_balance_ele)
        self.sleep(0.5)

    def to_about(self):
        """true:未登录，false:已登录"""
        self.swipe_find_ele(loc.myhome_about_ele, 'c', 'up')
        return self.is_eleExist(loc.login_user_ele)

    def red_withdraw(self):
        """红包提现"""
        self.click_element(loc.red_withdraw_ele)
        self.click_element(loc.red_bankcard_list_ele)
        self.click_element(loc.red_bankcard_ele)
        self.input_text(loc.red_withdraw_input_ele, '100')
        self.click_element(loc.red_withdraw_checkbox_ele)
        self.click_element(loc.red_withdraw_submit_ele)

    def check_success_msg(self):
        """获取操作成功提示"""
        num = 3
        while True:
            if self.is_eleExist(loc.red_withdraw_hint_ele):
                return True
            else:
                self.sleep(0.5)
                num -= 1
        return False

    def check_red_record(self):
        self.click_element(loc.red_record_ele)


if __name__ == '__main__':
    # LoginPage('12312').get_doc()
    pass
