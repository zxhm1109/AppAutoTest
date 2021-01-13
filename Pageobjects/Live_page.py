#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/12/17 15:20 
# @File      : Live_page.py
# @desc      :

from common.BasePage import BasePage
from Pagelocators import MallMedicine_locators as loc
from common.logger import Mylog
from appium.webdriver.common.mobileby import By

logger = Mylog('Live_page.py').getlog()

index_goroom_ele = (By.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView')
index_redpackage_ele = (By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[2]')

index_msm_list_ele=(By.CLASS_NAME,'android.widget.TextView')

class IndexPage(BasePage):

    def index_swipe_refresh(self):
        # 下划刷新列表
        self.swipe_direction('down', 10)

    def index_go_room(self):
        self.click_element(index_goroom_ele)

    def check_goromme(self):
        return self.is_eleExist(index_goroom_ele)

    def do_redapckage(self):
        self.click_element(index_redpackage_ele)

    def get_msg_texts(self):
        res=self.get_elements(index_msm_list_ele)
        logger.info(res)

