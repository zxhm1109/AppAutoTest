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

list_data = []


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
        ii = RWConfig().read_config_options_dict('TikTop')
        index = []
        if ii:
            dunm = max(ii.keys())
            redata = eval(ii[dunm])
            logger.info('福袋列表：{}'.format(ii[dunm]))
            for data in range(len(redata)):
                if parms in redata[data][2]:
                    index.append(data * 3)
            self.LuckyBag_list(index[::-1], 1, redata)
        else:
            if parms:
                luckybag_ctime = 'new UiSelector().textContains("{}")'.format(parms)
                luckybag_ctime_xpath = (BY.XPATH, "//android.view.View[@text='{}']".format(parms))
                # 划动到指定福袋位置
                if self.basep.is_eleExist(is_luckybag_num, 0):
                    self.basep.swipe_find_ele(luckybag_ctime, 'is', 'up', method=0)
                self.basep.swipe_direction('up', 5)
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
            self.LuckyBag_list(index[::-1], 0, redata)

    def LuckyBag_list(self, indexs, num, ini):
        # 遍历福袋列表，获得点击位置，点击进入福袋：parms=福袋创建时间 -1，parms=福袋名称 -2（福袋名称存在重复）
        ccnum = 1
        for lb in indexs:
            logger.info('---------->  开始执行福袋：{}   <--------'.format(ini[int(lb / 3)]))
            click_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                             lb + 2))
            name = (BY.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                        lb + 1))
            timec = (BY.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[{}]'.format(
                         lb + 3))
            check_ele = (BY.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]')

            while True:
                try:
                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(click_ele))
                    luckybag_name = self.driver.find_element(*name).text
                    timecc = self.driver.find_element(*timec).text
                    self.click(click_ele)
                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(check_ele))
                    self.basep.sleep(2)
                    self.get_plist(name, timec)
                    break
                except Exception:
                    if ccnum:
                        self.basep.swipe_direction('up', 1) if num else self.basep.swipe_direction('down', 1)
                        ccnum -= 1
                    else:
                        self.basep.swipe_direction('down', 1)
            lnum = int(ini[int(lb / 3)][0].split(':')[-1].strip())
            print('@@@@@@@@@@@@@@@@@@@@@@    {}'.format(lnum))
            self.consingee(luckybag_name, timecc, lnum)

    def get_plist(self, name, timec):
        # 获取 收货人列表
        self.basep.sleep(3)
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

    def consingee(self, name, timec, lnum):

        # 遍历中奖人：姓名、手机号；获取快递单ID，点击并填入快递单ID
        swip_num = 1
        bum = 0
        for iiii in range(lnum):
            self.get_plist(name, timec)
            global list_data
            data = list_data
            if '上传快递单' not in str(data):
                list_data = '没有可上传快递单的订单！！'
                break
            for yy in range(len(data)):
                if len(data[yy]) > 3:
                    if data[yy][-1] == '上传快递单':
                        cphone = str(data[yy][2][4:]).strip()
                        cname = str(data[yy][1][4:]).strip()
                        orderid = ExcelUtils().GetOrderId(phone=cphone, name=cname)
                        if orderid:
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
                                    self.basep.sleep(1)
                                    self.driver.find_element(*View_click_ele).click()
                                    logger.info('点击上传快递单：{}'.format(View_click_ele[1]))
                                    self.basep.sleep(1)
                                    WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(wuliuxinxi))
                                    self.basep.input_text(wuliuxinxi, orderid[0])
                                    # 手动选择快递公司
                                    self.basep.sleep(3)
                                    self.driver.find_element(*confirm_ele).click()
                                    self.basep.sleep(1)
                                    self.driver.find_element(*confirm_ele).click()
                                    logger.info('发货成功：{},{},{}'.format(View_name_ele, View_phone_ele, orderid))
                                    self.basep.sleep(1)
                                    self.basep.swipe_direction('down', 8)
                                    break
                                except Exception:
                                    self.basep.swipe_direction('up', swip_num)
                                    swip_num += 1
                            data[yy].append(orderid)
                            bum += 1
                        else:
                            data[yy].append(orderid)
                            logger.info('该订单已发货：{}'.format(data[yy]))
                    else:
                        data[yy].append('Excel中未找到该收货人')
                else:
                    data[yy].append('App收货信息缺失')

        logger.info('—————————————> 福袋 {} - {} 发货[{}] 处理完毕\n处理数据：{}'.format(name, timec, bum, list_data))
        self.basep.back()

    def Consignment(self, filename):
        ExcelUtils().ReadExcel(filename)
        # self.To_luckybag()
        input('\n\n----------------请先确定物流是否选择正确，点击进入福袋列表后Enter 继续！-----------\n\n')
        self.basep.sleep(1)
        ff = filename.split('-')[-1].split('.')[0]
        parms = ff[:4] + '/' + ff[4:6] + '/' + ff[6:]
        # parms = '2020/12/25 11:43'
        self.LuckyBag(parms=parms)

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
        fm = os.path.join('C:\\Users\\ai013\Desktop\WorkFile\TestFile\TikTopExpress\\', filename)
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
        global Excel_data
        Excel_data = test_data
        print(Excel_data)
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
            raise ValueError('Excel快递单号重复:{}'.format(reorderid))
        elif len(reconsignee):
            logger.error('Excel收货人重复：{}'.format(reconsignee))
        elif len(huanfa_data):
            logger.error('Excel运单号异常数据：{}'.format(huanfa_data))
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
            if phone in v['phone'] and name in v['name']:
                Excel_data.pop(k)
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


if __name__ == '__main__':
    # ExcelUtils().ReadExcel('抖音快递单-20201225.xls')
    # phone = ['15025445153', '13866233313']
    # name = ['杨婷', '小李']
    # for i in range(2):
    #     a,b = ExcelUtils().GetOrderId(name=name[i], phone=phone[i])
    # print(a, b)

    # ExcelUtils().check_Phone_reprat()

    # ctime = '2021/01/06 13:31'
    filename = '抖音快递单-20201225.xls'
    Test_TikTop().Consignment(filename)
