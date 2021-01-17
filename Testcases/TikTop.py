#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2021/1/6 17:43 
# @File      : TikTop.py 
# @desc      :

from appium import webdriver
from appium.webdriver.common.mobileby import By as BY
from common.BasePage import BasePage
import os, time, xlrd
from common.logger import Mylog
from common.DoConfig import RWConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

logger = Mylog('TikTop.py').getlog()

# 我的
myhome = (BY.XPATH,
          '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/dmt.viewpager.DmtViewPager.d/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.RelativeLayout')
# 更多设置
more = (BY.XPATH, '//android.widget.ImageView[@content-desc="更多"]')
# 取消App更新
cancel_version_update = (BY.ID,
                         'com.ss.android.ugc.aweme:id/dqt')
# 企业服务中心
enterprice_service = (BY.XPATH, '//android.widget.RelativeLayout[@content-desc="企业服务中心"]')
# 主播中心
anchor_centre = (BY.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup')
anchor_contains = 'new UiSelector().textContains("主播中心")'

# 福袋列表入口
luckybag = (BY.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[12]/android.view.View')
luckybag_contains = 'new UiSelector().textContains("福袋")'
luckybag_record = (BY.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.Vie')

# 福袋列表 数量、时间
is_luckybag_num = 'new UiSelector().textContains("100人获取福袋")'

end_luckybag_record = 'new UiSelector().textContains("2020/12/25 11:43")'

# 上传快递单
upload_orderid = (BY.XPATH, '')
upload_orderid_comfirm = ()

Excel_data = {}
HuanfaData = {}

list_data = []

top_ele = (BY.XPATH,
           "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View[7]")

logger.info('开始抖音发货')

indexs = []
num = 0
ini = ''
newconsingee_off = True


class Test_TikTop:
    """
    抖音福袋自动发货
    """

    def __init__(self):
        self.logger = Mylog('TikTop.py').getlog()
        # caps = {
        #     "platformName": "Android",
        #     "platformVersion": "6.0.1",
        #     "deviceName": "54c752a8",
        #     "appPackage": "com.ss.android.ugc.aweme",
        #     "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
        #     "noReset": "true",
        #     "automationName": "UiAutomator1"
        # }
        caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "NAB5T20506007667",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
            , "noReset": "true", "automationName": "UiAutomator1"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.basep = BasePage(self.driver)

    def To_luckybag(self):
        """
        操作 进入福袋列表页
        :return:
        """
        # 点击我的，跳转个人中心
        # self.click(myhome)
        # 点击右下角
        size = self.basep.get_size()
        print('当前屏幕大小：{}'.format(size))
        tap_lower_right = [int(size['width']) - 80, int(size['height']) - 11]
        # self.basep.click_tap([1000, 2200])
        self.basep.sleep(5)
        self.basep.click_tap(tap_lower_right)
        # 点击右上角 ≡  展开更多功能
        self.click(more)
        # 点击企业服务中心
        self.click(enterprice_service)
        # 点击主播中心
        self.basep.sleep(1)
        # self.click(anchor_centre)
        self.basep.click_element(anchor_contains)
        # 点击福袋
        self.basep.swipe_direction('up', 2)
        # self.basep.swipe_find_ele(luckybag_contains, 'c', 'up', method=0)
        self.click(luckybag_contains)

    def LuckyBag(self, parms=None):
        """
        进入指定福袋，获取收货人信息
        :param parms: 福袋创建时间
        :return: 收货人列表、指定福袋以上的所有福袋信息列表
        """
        # 获取福袋
        global indexs, num, ini
        ii = RWConfig().read_config_options_dict('TikTop')
        index = []
        if ii:
            dunm = max(ii.keys())
            redata = eval(ii[dunm])
            logger.info('福袋列表：{}'.format(ii[dunm]))
            for data in range(len(redata)):
                if parms in redata[data][2]:
                    index.append(data * 3)
            indexs = index[::-1]
            num = 1
            ini = redata
        else:
            if parms:
                luckybag_ctime = 'new UiSelector().textContains("{}")'.format(parms)
                luckybag_ctime_xpath = (BY.XPATH, "//android.view.View[@text='{}']".format(parms))
                # 划动到指定福袋位置
                if self.basep.is_eleExist(is_luckybag_num, 0):
                    self.basep.swipe_find_ele(luckybag_ctime, 'is', 'up', method=0)

                # 获取当前所有福袋名称、创建时间、发放数量
                LuckBagRecord = []
                dunm = 0
                logger.info('——————————————开始读取福袋列表数据')
                eles = self.driver.find_elements_by_class_name('android.view.View')
                for ele in eles:
                    text = ele.text
                    LuckBagRecord.append(text)
                lbr = list(filter(None, LuckBagRecord))
                luckybaglist = []
                if lbr[0] == '福袋记录':
                    lbr.pop(0)
                    if len(lbr) % 3 != 0:
                        logger.info('获取福袋列表数据有问题')
                    else:
                        luckybaglist, luckybagdict = self.list_of_groups(lbr, 3)
                # 检查福袋中奖名单是否有重复数据
                # ExcelUtils().check_data()
                RWConfig().write_config('TikTop', str(dunm + 1), str(lbr)) if dunm else RWConfig().write_config('TikTop', '1', str(luckybaglist))
            else:
                logger.error('parms缺失！！！')
            ii = RWConfig().read_config_options_dict('TikTop')
            logger.info('福袋列表：{}'.format(ii))
            logger.info('_________________________________')
            dunm = max(ii.keys())
            redata = eval(ii[dunm])
            for data in range(len(redata)):
                if parms in redata[data][2]:
                    index.append(data * 3)
            for i in index:
                print(redata[i])
            indexs = index[::-1]
            num = 1
            ini = redata

        self.LuckyBag_list()

    def LuckyBag_list(self):
        global indexs, num, ini
        # 遍历福袋列表，获得点击位置，点击进入福袋：parms=福袋创建时间 -1，parms=福袋名称 -2（福袋名称存在重复）
        fail = []
        for lb in indexs:

            click_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                             lb + 2))
            name = (BY.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                        lb + 1))
            timec = (BY.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                         lb + 3))
            luckybag_name = self.driver.find_element(*name).text
            timecc = self.driver.find_element(*timec).text
            check_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]')

            while True:
                try:
                    self.click(click_ele)
                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(check_ele))
                    self.basep.sleep(1)
                    break
                except Exception:
                    if num:
                        self.basep.swipe_direction('down', 1, 7, 1000)
                    else:
                        self.basep.swipe_direction('up', 1, 7, 1000)

            lnum = int(ini[int(lb / 3)][0].split(':')[-1].strip())
            print('@@@@@@@@@@@@@@@@@@@@@@    {} == {}'.format(lnum, str(luckybag_name)))

            # self.consingee(luckybag_name, timecc, lnum)
            # 更新从最后一个开始发货
            for i in range(8):
                try:
                    logger.info('[{}]---------->  开始执行福袋：{} - {}  <--------'.format(i + 1, luckybag_name, timecc))
                    self.newconsingee(luckybag_name, timecc, lnum)
                    self.newget_plist(luckybag_name, timecc, 0)
                    self.basep.sleep(2)
                    self.basep.back()
                    break
                except RuntimeError:
                    pass
            else:
                logger.error('{} - {} 八次重试依然失败!!!结束该福袋,继续下一个福袋!'.format(luckybag_name, timecc))
                fail.append([luckybag_name, timecc])
                self.newget_plist(luckybag_name, timecc, 0)
                self.basep.sleep(2)
                self.basep.back()
        logger.info('执行结束! 失败福袋:{}'.format(fail))

    def get_plist(self, name, timec):
        # 获取 收货人列表
        self.basep.sleep(2)
        logger.info('—————————————> 开始获取福袋 {} - {} 的收货人信息'.format(name, timec))
        eless = self.driver.find_elements_by_class_name('android.view.View')
        consignee_list = []
        for rele in eless:
            text = rele.text
            if text == '上传快递单':
                consignee_list.append(text)
                break
            consignee_list.append(text)

        # 去除空白字符、福袋信息和确定、取消
        consignee = list(filter(None, consignee_list))
        new_consignee = consignee[7:] if '人获得福袋）' in consignee[6] and '上传快递单' in consignee[-1] else consignee[7:-2]
        logger.debug('抖音福袋:{} -- 收货人列表:{}'.format(name, new_consignee))
        # 根据每个收货人给list分组
        data = []
        datalist = []
        for ii in new_consignee:
            if '上传快递单' == ii or '提醒一下' == ii or '收货信息：逾期未填写' == ii or '修改快递单' == ii:
                datalist.append(ii)
                data.append(datalist)
                datalist = []
            else:
                datalist.append(ii)
        logger.debug('处理后收货人数据：{}'.format(data))
        global list_data
        if data == list_data:
            logger.info('-----list_data不需要更新，现有数据量{}'.format(len(list_data)))
            return False
        else:
            list_data = data
            logger.info('-----更新list_data数据！ 更新数据量:{}'.format(len(list_data)))
            return True

    def newget_plist(self, name, timec, iszx=1):
        # 获取 收货人列表
        self.basep.sleep(2)
        consignee_list = []
        try:
            a = eval(RWConfig().read_config_options_dict('Rett')[str(timec).replace(' ', '').replace('/', '').replace(':', '')])
        except KeyError:
            a = ['111']
        if a[-1] == '确定':
            logger.info('{}:没有可处理的订单!'.format(timec))
            return False, False
        logger.info('{} - {}   开始加载收货人列表!!!!!!!'.format(name, timec))
        eless = self.driver.find_elements_by_class_name('android.view.View')
        for rele in eless:
            text1 = rele.text
            consignee_list.append(text1)
            if iszx:
                if '上传快递单' == str(text1).strip():
                    consignee = list(filter(None, consignee_list))
                    lphone = consignee[-3][4:]
                    lname = consignee[-4][4:]
                    a, b = ExcelUtils().GetOrderId(lphone, lname)
                    if b:
                        logger.info('{}:有未处理的订单!'.format(timec))
                        return True, len(consignee)
                    else:
                        logger.info('{}:手机号:{} 没有匹配到运单号!'.format(timec, lphone))
            else:
                pass
        else:
            consignee = list(filter(None, consignee_list))
            RWConfig().write_config('Rett', str(timec).replace(' ', '').replace('/', '').replace(':', ''), str(consignee))
            logger.info('{}:没有可处理的订单!'.format(timec))
            return False, False

    def newconsingee(self, name, timec, lnum):

        # 遍历中奖人：姓名、手机号；获取快递单ID，点击并填入快递单ID
        unfind = 0
        bum = 0
        result = {'succeed': [], 'fail': []}
        orderid = [0, 0]
        aaa, bbb = self.newget_plist(name, timec)
        top = 0
        if aaa:
            if (bbb // 5) < (lnum // 2):
                logger.info('{}  从头部开始执行!!'.format(bbb // 5))
                self.basep.swipe_direction('down', 10, 9, 500)
            else:
                logger.info('{}  从尾部开始执行!!'.format(bbb // 5))
                self.basep.swipe_direction('up', 10, 9, 500)
                top = 1
            for yy in (reversed(range(lnum)) if top else (range(lnum))):
                index = yy + 8
                View_nickname_ele = 'undefined'
                try:
                    View_nickname_ele = self.driver.find_element(BY.XPATH,
                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                     index, 2)).text
                    View_click_ele = (BY.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[6]".format(
                                          index))
                    click_name_ele = self.driver.find_element(*View_click_ele).text

                except NoSuchElementException:
                    unfind += 1
                    logger.info('{} - {}:用户发货信息缺失,无法发货!!'.format(index, View_nickname_ele))
                    if unfind > 1:
                        self.basep.swipe_direction('down', num=1, distance=0.7, ctime=1000) if top else self.basep.swipe_direction('up', 1, 0.7, 1000)
                    continue
                print('asdsads22222222222222adas:' + str(click_name_ele), type(click_name_ele))
                if '上传快递单' in click_name_ele:
                    View_name_ele = self.driver.find_element(BY.XPATH,
                                                             "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                 index, 3)).text
                    View_phone_ele = self.driver.find_element(BY.XPATH,
                                                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                  index, 4)).text
                    View_addr_ele = self.driver.find_element(BY.XPATH,
                                                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[5]'.format(
                                                                 index)).text
                    orderid = ExcelUtils().GetOrderId(phone=View_phone_ele[4:], name=View_name_ele[4:])
                    logger.info('[{}] 执行发货：{},{} \n\t\t\t\t发货内容：{}'.format(index, View_name_ele, View_phone_ele, orderid))
                elif '韵达速递' in click_name_ele:  # 修改快递单
                    View_name_ele = self.driver.find_element(BY.XPATH,
                                                             "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                 index, 3)).text
                    View_phone_ele = self.driver.find_element(BY.XPATH,
                                                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                  index, 4)).text
                    View_addr_ele = self.driver.find_element(BY.XPATH,
                                                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[5]'.format(
                                                                 index)).text
                    unfind += 1
                    if unfind > 1:
                        if len(View_addr_ele) > 20:
                            self.basep.swipe_direction('down', num=1, distance=1, ctime=1000) if top else self.basep.swipe_direction('up', 1,
                                                                                                                                     1,
                                                                                                                                     1000)
                            continue
                        else:
                            self.basep.swipe_direction('down', num=1, distance=0.9, ctime=1000) if top else self.basep.swipe_direction('up', 1,
                                                                                                                                       0.9,
                                                                                                                                       1000)
                            continue
                else:
                    print('\n\n\n\n\t\t\t\t\t 未知异常 \n\n\n\n')
                    continue

                hhanum = 1
                confirm_ele = (BY.XPATH,
                               "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[2]/android.view.View[5]".format(
                                   int(lnum) + 8))
                wuliuxinxi = (BY.CLASS_NAME, "android.widget.EditText")
                while orderid[0]:
                    try:
                        self.basep.sleep(2)
                        logger.info('第{}次点击上传快递单：{}'.format(hhanum, View_click_ele[1][-30:]))
                        local = True
                        lllnum = 0
                        while local:
                            try:
                                local = self.driver.find_element(*View_click_ele).location
                                print('\t\t\t\t\t\t\t\t\t\t当前按钮位置:{}'.format(local))
                                if local['y'] < 500:
                                    self.basep.swipe_direction('down', num=1, distance=1, ctime=1000)
                                if local['y'] > 2060:
                                    self.basep.swipe_direction('up', 1, 1, 1000)
                                else:
                                    local = False
                                    self.driver.find_element(*View_click_ele).click()
                                    self.basep.sleep(1)
                                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(wuliuxinxi))
                            except Exception:
                                print('\t\t\t\t\t [{}]  调整按钮在当前屏幕的位置！'.format(lllnum))
                                lllnum += 1
                                if lllnum < 5:
                                    self.basep.swipe_direction('down', num=1, distance=8, ctime=1000)
                                elif lllnum > 5:
                                    self.basep.swipe_direction('up', 1, 8, 1000)
                                elif lllnum == 5:
                                    self.basep.swipe_direction('up', 5, 8, 1000)
                                else:
                                    logger.error('福袋 {} - {}发货异常失败!!重新开始发货'.format(name, timec))
                                    raise RuntimeError

                        # self.driver.find_element(*View_click_ele).click()
                        # self.basep.sleep(1)
                        # WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(wuliuxinxi))
                        # aaaa = 0
                        try:
                            self.basep.input_text(wuliuxinxi, str(orderid[0]))
                            self.basep.sleep(3)
                            self.driver.find_element(*confirm_ele).click()
                            self.basep.sleep(1)
                            aaaa = len(str(self.driver.find_element(*wuliuxinxi).text))
                            self.basep.click_tap([520, 2090], 1)
                        except Exception:
                            aaaa = 0

                        wunm = 0
                        while aaaa > 15 or aaaa < 12:
                            print('\t\t\t\t\t第 {} 次输入运单号'.format(wunm))
                            wunm += 1
                            if wunm == 10:
                                raise RuntimeError
                            try:
                                xxxlocal =self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("顺丰速递")').location
                                self.driver.back()
                            except Exception:
                                pass
                            try:
                                self.basep.sleep(1)
                                try:
                                    kkkk = self.driver.find_element(*wuliuxinxi).location
                                except Exception:
                                    self.driver.find_element(*View_click_ele).click()
                                self.basep.sleep(1)
                                self.basep.input_text(wuliuxinxi, str(orderid[0]))
                                self.basep.sleep(4)
                                self.driver.find_element(*confirm_ele).click()
                                self.basep.sleep(1)
                                aaaa = len(str(self.driver.find_element(*wuliuxinxi).text))
                                self.basep.click_tap([520, 2090], 1)
                                self.basep.sleep(1)
                            except Exception:
                                aaaa = 0
                        print('输入运单号长度: {}'.format(aaaa))
                        self.basep.sleep(3)
                        # self.driver.find_element(*confirm_ele).click()
                        self.basep.click_tap([520, 2090], 1)
                        self.basep.sleep(1)
                        if unfind > 1:
                            self.basep.swipe_direction('down', num=1, distance=0.9, ctime=1000) if top else self.basep.swipe_direction('up', 1,
                                                                                                                                       0.9,
                                                                                                                                       1000)
                        unfind += 1
                        bum += 1
                        result['succeed'].append(str(View_phone_ele) + '：' + str(orderid))
                        logger.info('{}:发货成功：{},{},{}'.format(index, View_name_ele, View_phone_ele, orderid))
                        break
                    except Exception:
                        logger.error('—————————————> 福袋 {} - {}发货异常失败!!重新开始发货'.format(name, timec))
                        raise RuntimeError
                else:
                    if unfind > 1:
                        if len(View_addr_ele) > 20:
                            self.basep.swipe_direction('down', num=1, distance=0.9, ctime=1000) if top else self.basep.swipe_direction('up', 1, 0.9,
                                                                                                                                       1000)
                        else:
                            self.basep.swipe_direction('down', num=1, distance=0.8, ctime=1000) if top else self.basep.swipe_direction('up', 1, 0.8,
                                                                                                                                       1000)
                    unfind += 1
                    result['fail'].append(str(View_phone_ele) + "-" + str(View_name_ele) + "：Excel中未找到该收货人")
                    logger.info('{}:Excel中未找到该收货人'.format(index))
        RWConfig().write_config('TTResult', str(timec).replace(' ', '').replace('/', '').replace(':', ''), str(result))
        logger.info('—————————————> 福袋 {} - {} 发货[{}] 处理完毕\n\t\t\t\t\t\t处理数据：{}'.format(name, timec, bum, list_data))

    def consingee(self, name, timec, lnum):
        # 遍历中奖人：姓名、手机号；获取快递单ID，点击并填入快递单ID
        bum = 0
        for iiii in range(lnum):
            self.get_plist(name, timec)
            global list_data
            data = list_data
            if '上传快递单' not in str(data):
                logger.info('没有可上传快递单的订单！！')
                break
            for yy in range(len(data)):
                if len(data[yy]) > 3:
                    if data[yy][-1] == '上传快递单':
                        swip_num = 1
                        cphone = str(data[yy][2][4:]).strip()
                        cname = str(data[yy][1][4:]).strip()
                        orderid = ExcelUtils().GetOrderId(phone=cphone, name=cname)
                        if orderid[0]:
                            index = yy + 8
                            View_name_ele = self.driver.find_element(BY.XPATH,
                                                                     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                         index, 3)).text
                            View_phone_ele = self.driver.find_element(BY.XPATH,
                                                                      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[{}]".format(
                                                                          index, 4)).text

                            View_click_ele = (BY.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[6]".format(
                                                  index))

                            confirm_ele = (BY.XPATH,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[{}]/android.view.View[2]/android.view.View[5]".format(
                                               int(lnum) + 8))

                            wuliuxinxi = (BY.CLASS_NAME, "android.widget.EditText")

                            logger.info('查找收货人：{}\n\t\t执行发货：{},{} \n\t\t发货内容：{}'.format(data[yy], View_name_ele, View_phone_ele, orderid))
                            while True:
                                try:
                                    self.basep.sleep(2)
                                    logger.info('第{}次点击上传快递单：{}'.format(swip_num, View_click_ele[1][-30:]))
                                    self.driver.find_element(*View_click_ele).click()
                                    self.basep.sleep(1)
                                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(wuliuxinxi))
                                    # self.basep.input_text(wuliuxinxi, orderid[0])
                                    self.driver.find_element(*wuliuxinxi).send_keys(str(orderid[0]))
                                    # 手动选择快递公司
                                    self.basep.sleep(2)
                                    self.driver.find_element(*confirm_ele).click()
                                    self.basep.sleep(1)
                                    self.driver.find_element(*confirm_ele).click()
                                    logger.info('发货成功：{},{},{}'.format(View_name_ele, View_phone_ele, orderid))
                                    self.basep.sleep(1)
                                    if index < 20 and swip_num > 2:
                                        self.driver.find_element(*top_ele).click()
                                    else:
                                        self.basep.swipe_direction('up', num=1, distance=1)
                                    break
                                except Exception:
                                    self.basep.swipe_direction('up', num=swip_num, distance=8, ctime=1000)
                                    swip_num += 1
                            data[yy].append(orderid)
                            bum += 1
                        else:
                            data[yy].append('Excel中未找到该收货人')
                            logger.info('Excel中未找到该收货人')
                    else:
                        data[yy].append('该订单无法发货')
                        logger.info('该订单无法发货')
                else:
                    data[yy].append('App收货信息缺失')
                    logger.info('App收货信息缺失')
        logger.info('—————————————> 福袋 {} - {} 发货[{}] 处理完毕\n处理数据：{}'.format(name, timec, bum, list_data))
        self.basep.back()

    def Consignment(self, filename):

        input('\n\n----------------请先确定物流是否选择正确，点击进入福袋列表后Enter 继续！-----------\n\n')
        for file in filename:
            ExcelUtils().ReadExcel(file)
            # self.To_luckybag()
            # self.basep.swipe_direction('up', distance=7, num=3, ctime=1000)
            self.basep.sleep(1)
            ff = file.split('-')[-1].split('.')[0]
            parms = ff[:4] + '/' + ff[4:6] + '/' + ff[6:]
            # parms = '2020/12/25 11:43'
            self.LuckyBag(parms=parms)
        ExcelUtils().check_run_data()

    def click(self, loc):
        """
        检查是否弹出App更新提示，若出现则点击取消更新
        :param loc:
        :return:
        """
        self.basep.sleep(2)
        # if self.basep.is_eleExist(cancel_version_update):
        #     self.basep.click_element(cancel_version_update)
        self.basep.click_element(loc)

    def list_of_groups(self, list_info, per_list_len):
        '''
        给福袋记录列表根据福袋分组
        :param list_info:   福袋列表
        :param per_list_len:  每个小列表的长度（3）
        :return:
        '''
        luckybagdict = []
        list_of_group = zip(*(iter(list_info),) * per_list_len)
        end_list = [list(i) for i in list_of_group]
        count = len(list_info) % per_list_len
        end_list.append(list_info[-count:]) if count != 0 else end_list
        if len(end_list):
            for i in end_list:
                lt = {}
                lt['name'] = i[0]
                lt['num'] = i[1][:4]
                lt['ctime'] = i[2]
                luckybagdict.append(lt)
        return end_list, luckybagdict


class ExcelUtils:

    def GetFilePath(self):
        """
        遍历 TikTopExpress 文件夹下所有文件，返回 最新创建的文件
        :return:
        """
        fc = {}
        # 获取文件夹下的所有文件名
        file_name_list = os.listdir(r'C:\Users\ai013\Desktop\WorkFile\TestFile\TikTopExpress\\')
        for file_name in file_name_list:
            if '$' not in file_name:
                file_path = r'C:\Users\ai013\Desktop\WorkFile\TestFile\TikTopExpress\{}'.format(file_name)
                # 获取文件创建时间
                ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getctime(file_path)))
                fc[ctime] = file_name
        fn = max(fc.keys())
        return 'C:\\Users\\ai013\Desktop\WorkFile\TestFile\TikTopExpress\\{}'.format(fc[fn])

    def ReadExcel(self, filename):
        """
        1、读取Excel，获取快递单号、收货人手机号、收货人姓名
        2、检查Excel数据是否存在重复数据
        3、缺少福袋信息（福袋名称、创建/发布时间）
        :return: ｛orderID:｛phone,name｝,orderID2:{phone,name}...｝
        """
        fm = os.path.join('D:\TikTopExpress\\', filename)
        # 读取 Excel
        f = xlrd.open_workbook(fm)
        ws = f.sheet_by_index(0)
        test_data = {}
        huanfa_data = {}
        for row in range(1, ws.nrows):
            row_data = {}
            orderId = str(ws.cell_value(row, 3))
            if self.is_str(orderId):
                phone = str(ws.cell_value(row, 5))
                name = str(ws.cell_value(row, 4))
                exm = str(ws.cell_value(row, 2))
                row_data['phone'] = phone
                row_data['name'] = name.strip(' ')
                row_data['exm'] = exm
                test_data[orderId] = row_data
            else:
                phone = str(ws.cell_value(row, 5))
                name = str(ws.cell_value(row, 4))
                exm = str(ws.cell_value(row, 2))
                row_data['phone'] = phone
                row_data['name'] = name.strip(' ')
                row_data['exm'] = exm
                huanfa_data[orderId] = row_data
        global Excel_data, HuanfaData
        Excel_data = test_data
        HuanfaData = huanfa_data
        logger.debug('Excel待处理快递单数量：{}，待处理快递单：{}'.format(len(test_data), test_data))

    def check_data(self, data):
        """
        检查列表数据是否有重复数据
        :return: 有重复时 打印重复数据，返回 False
        """
        v, rv = [], []
        for k in data:
            if k not in v:
                v.append(k)
            else:
                rv.append(k)
        if len(rv):
            logger.error('重复数据：{}'.format(rv))
            return False
        else:
            return True

    def GetOrderId(self, phone, name):
        """
        根据 收货人姓名、收货人手机号 获取快递单号
        :param phone:收货人手机号
        :param name:收货人姓名
        :return:
        """
        global Excel_data
        num = len(Excel_data)
        logger.info('Excel_data数据：{}'.format(Excel_data))
        for k, v in Excel_data.items():
            if phone in v['phone']:
                # Excel_data.pop(k)
                logger.info('Excel取出数据：{}:{}:{}'.format(v['name'], v['phone'], k))
                if len(Excel_data) / num == 0.5:
                    logger.info('Excel数据已处理50%')
                elif len(Excel_data) == 0:
                    logger.info('Excel数据已处理完毕')
                return k, v
        else:
            logger.error('Excel未找到该收货人：{},{}'.format(name, phone))
            return None, None

    def is_str(self, str):
        """是否包含中文"""
        for c in str:
            if ord(c) > 255:
                return False
            else:
                return True

    def check_run_data(self):
        rundata = RWConfig().read_config_options_dict('Rett')
        for k, v in rundata.items():
            filename = '抖音快递单-' + str(k[:-4]) + '.xls'
            un_result = {}
            self.ReadExcel(filename)

            run_data_num = v[5]
            new_consignee = v[7:] if '人获得福袋）' in v[6] and '上传快递单' in v[-1] else v[7:-2]
            # 根据每个收货人给list分组
            run_data = []
            datalist = []
            run_end_data = []
            for ii in new_consignee:
                if '上传快递单' == ii or '提醒一下' == ii or '收货信息：逾期未填写' == ii or '修改快递单' == ii:
                    datalist.append(ii)
                    run_data.append(datalist)
                    datalist = []
                else:
                    datalist.append(ii)
            if int(run_data_num) == len(run_data):
                logger.info('给App收货人分组,得到 {} 个收货人'.format(len(run_data)))
                for i in run_data:  # 每个收货人
                    for ix in range(len(i)):
                        if '韵达速递' in i[ix]:
                            self.check_run_excel(i, ix, k, 1)
                        elif '上传快递单' in i[ix]:
                            self.check_run_excel(i, ix, k, 2)
                        elif '收货信息：逾期未填写' in i[ix] or '提醒一下' in i[ix]:
                            self.check_run_excel(i, ix, k, 3)
                logger.info('{} 福袋检查完毕，结果数据以保存'.format(str(k[:-4])))
            else:
                logger.error('[{}]  Rett数据与福袋数量不一致: {} != {}'.format(str(k[:-4]), run_data_num, str(len(run_data))))
                RWConfig().write_config('CheckResult', str(k[:-4]), 'None')

    def check_run_excel(self, i, ix, k, method):
        filename1 = '抖音快递单-' + str(k[:-4]) + '.xls'
        logger.info('开始检查 {} 福袋: nickname: {}'.format(str(k[:-4]), i[ix - 4]))
        consigee_result = {'succeed': [], 'orderfail': [], 'phonefail': [], 'namefail': [], 'undefined': [], 'huanfa': [], 'overdue': []}
        self.ReadExcel(filename1)
        global Excel_data, HuanfaData
        aa = {}
        for k, v in Excel_data.items():
            if method == 1:
                if i[ix][6:] == k:
                    aa[k] = {'nickname': i[0], 'phone': i[ix - 2][4:], 'name': i[ix - 3][4:]}
                    logger.info('匹配到快递单:{}'.format(i[ix][6:]))
                    if i[ix - 2][4:] in v['phone']:
                        logger.info('匹配到手机号:{}'.format(i[ix - 2][4:]))
                        if i[ix - 3][4:] in v['name']:
                            logger.info('匹配到姓名:{}'.format(i[ix - 3][4:]))
                            consigee_result['succeed'].append(aa)
                        else:
                            logger.info('{} - {} 没有匹配到姓名:{}'.format(i[0], i[ix - 2][4:], i[ix - 3][4:]))
                            consigee_result['namefail'].append(aa)
                    else:
                        logger.error('{} - {} 没有匹配到手机号:{}'.format(i[0], i[ix - 2][4:], i[ix - 2][4:]))
                        consigee_result['phonefail'].append(aa)
                else:
                    logger.info('{} - {} 没有匹配到快递单:{}'.format(i[0], i[ix - 2][4:], k))
                    consigee_result['orderfail'].append(aa)
            elif method == 2:
                if i[ix - 2][4:] in v['phone']:
                    aa[k] = {'nickname': i[0], 'phone': i[ix - 2][4:], 'name': i[ix - 3][4:]}
                    logger.info('遗漏发货人[ {}: {} - {} ], 需重新发货'.format(k, i[ix - 2][4:], i[ix - 3][4:]))
                    consigee_result['undefined'].append(aa)
                else:
                    for kk, vv in HuanfaData.items():
                        if i[ix - 2][4:] in vv['phone']:
                            logger.info('缓发 [ {} - {} ], 等待发货中！'.format(i[ix - 2][4:], i[ix - 3][4:]))
                            consigee_result['huanfa'].append(aa)
            elif method == 3:
                aa[i[0]] = {i[1]}
                logger.info('用户 [ {} ] 收货信息信息未填写！'.format(i[0]))
                consigee_result['overdue'].append(aa)
            else:
                pass
        RWConfig().write_config('CheckResult', str(k[:-4]), str(consigee_result))


if __name__ == '__main__':
    # ExcelUtils().ReadExcel('抖音快递单-20201225.xls')
    # phone = ['15025445153', '13866233313']
    # name = ['杨婷', '小李']
    # for i in range(2):
    #     a,b = ExcelUtils().GetOrderId(name=name[i], phone=phone[i])
    # print(a, b)

    # ExcelUtils().check_Phone_reprat()

    # ctime = '2021/01/06 13:31'
    resss = ['抖音快递单-20201225.xls']
    filename = ['抖音快递单-20201227.xls', '抖音快递单-20201228.xls', '抖音快递单-20201229.xls', '抖音快递单-20201230.xls']
    Test_TikTop().Consignment(filename)
