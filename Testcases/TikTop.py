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

# 福袋列表 数量、第一个福袋时间
is_luckybag_num = 'new UiSelector().textContains("100人获取福袋")'
end_luckybag_record = 'new UiSelector().textContains("2020/12/25 11:43")'

# 上传快递单
upload_orderid = (BY.XPATH, '')
upload_orderid_comfirm = ()


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
        self.basep.click_tap(tap_lower_right)
        # 点击右上角 ≡  展开更多功能
        self.click(more)
        # 点击企业服务中心
        self.click(enterprice_service)
        # 点击主播中心
        # self.click(anchor_centre)
        self.basep.sleep(1)
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
        luckybag_ctime = 'new UiSelector().textContains("{}")'.format(parms)
        LuckBagRecord = []
        # 划动到指定福袋位置
        if self.basep.is_eleExist(is_luckybag_num, 0):
            self.basep.swipe_find_ele(luckybag_ctime, 'is', 'up', method=0)
            self.basep.swipe_direction('up', 3)

            # 获取当前所有福袋名称、创建时间、发放数量
            eles = self.driver.find_elements_by_class_name('android.view.View')
            for ele in eles:
                text = ele.text
                LuckBagRecord.append(text)
        lbr = list(filter(None, LuckBagRecord))

        # 遍历福袋列表，获得点击位置，点击进入福袋：parms=福袋创建时间 -1，parms=福袋名称 +1（福袋名称存在重复）
        for lb in range(len(lbr)):
            if lbr[lb] == parms:
                click_ele = (BY.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                                 lb - 1))
                self.click(click_ele)
                break

        # 获取 收货人列表
        eless = self.driver.find_elements_by_class_name('android.view.View')
        consignee_list = []
        for rele in eless:
            text = rele.text
            consignee_list.append(text)

        # 去除空白字符、福袋信息和确定、取消
        consignee = list(filter(None, consignee_list))
        new_consignee = consignee[7:-2] if '人获得福袋）' in consignee[6] and '确定' in consignee[-1] else consignee

        # 根据每个收货人给list分组
        data = []
        datalist = []
        for ii in new_consignee:
            if '上传快递单' == ii or '提醒一下' == ii:
                data.append(datalist)
                datalist = []
            else:
                datalist.append(ii)
        print(consignee_list)
        return consignee_list, lbr

        # print(lbr)
        # if lbr[0] == '福袋记录':
        #     lbr.pop(0)
        #     if len(lbr) % 3 != 0:
        #         logger.info('获取福袋列表数据有问题')
        #     else:
        #         luckybaglist, luckybagdict = self.list_of_groups(lbr, 3)
        # print(luckybagdict)

        # 检查福袋中奖名单是否有重复数据
        # ExcelUtils().check_data()

    def Consignment(self, parms):
        self.To_luckybag()
        self.basep.sleep(3)
        consignee_list, lbr = self.LuckyBag(parms)

        # 遍历中奖人：姓名、手机号；获取快递单ID，点击并填入快递单ID
        for yy in range(len(consignee_list)):
            if len(consignee_list[yy]) > 2:
                orderid = ExcelUtils().GetOrderId(phone=consignee_list[yy][2][4:], name=consignee_list[yy][1][4:])
                if orderid:
                    consignee_list[yy].append(orderid)
                    #
                else:
                    consignee_list[yy].append('Excel中未找到该收货人')
            else:
                print(consignee_list[yy], '收货信息缺失')

        print('结束')

    def click(self, loc):
        """
        检查是否弹出App更新提示，若出现则点击取消更新
        :param loc:
        :return:
        """
        self.basep.sleep(3)
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

    def ReadExcel(self):
        """
        1、读取Excel，获取快递单号、收货人手机号、收货人姓名
        2、检查Excel数据是否存在重复数据
        3、缺少福袋信息（福袋名称、创建/发布时间）
        :return: ｛orderID:｛phone,name｝,orderID2:{phone,name}...｝
        """

        # 读取 Excel
        f = xlrd.open_workbook(self.GetFilePath())
        ws = f.sheet_by_name('Sheet1')
        test_data = {}
        for row in range(1, ws.nrows):
            row_data = {}
            orderId = str(ws.cell_value(row, 1))
            phone = str(ws.cell_value(row, 11))
            name = str(ws.cell_value(row, 10))

            row_data['phone'] = phone
            row_data['name'] = name.strip(' ')
            test_data[orderId] = row_data

        # 检查数据是否重复
        orderid, reorderid, consignee, reconsignee = [], [], [], []
        for k, v in test_data.items():
            if k not in orderid:
                orderid.append(k)
            else:
                reorderid.append(k)
            if v not in consignee:
                consignee.append(v)
            else:
                reconsignee.append(v)

        if len(reorderid):
            raise ValueError('快递单号重复:{}'.format(reorderid))
        elif len(reconsignee):
            logger.error('收货人重复：{}'.format(reconsignee))

        logger.debug('待处理快递单数量：{}，待处理快递单：{}'.format(len(test_data), test_data))
        return test_data

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
        jh = self.ReadExcel()
        num = len(jh)
        logger.debug('预备备数据：{}'.format(jh))
        for k, v in jh.items():
            if v['phone'] == phone and v['name'] == name:
                jh.pop(k)
                logger.info('取出数据：{}:{}:{}'.format(v['name'], v['phone'], k))
                if len(jh) / num == 0.5:
                    logger.info('Excel数据已处理50%')
                elif len(jh) == 0:
                    logger.info('Excel数据已处理完毕')
                return k, v
            else:
                logger.error('未找到该收货人：{},{}'.format(name, phone))
                return None


if __name__ == '__main__':
    # phone = '18118415482'
    # name = '　许先生'
    # c = {'YT2115470846111': {'phone': '17857960558', 'name': '邓艳'}, 'YT2115467109736': {'phone': '13512743983', 'name': '程小姐'}}
    # a = ExcelUtils().GetOrderId(phone, name)
    # print(a)

    # ExcelUtils().check_Phone_reprat()

    ctime = '2021/01/06 13:31'
    Test_TikTop().Consignment()
