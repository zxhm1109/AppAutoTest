#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/8/21 14:00 
# @File      : login_page.py 
# @desc      : 登录页面 及 免费变美专区

from Pagelocators import login_locators as loc
from common.BasePage import BasePage

class LoginPage(BasePage):

    def FreeZone_loginORregister(self):
        doc="免费变美专区登录&注册"
        self.input_text(locator=loc.login_freeZone_phone,text="17621757807",doc=doc)
        self

