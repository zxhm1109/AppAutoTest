#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:54
# @File      : BasePage.py
# @desc      :

from common.logger import Mylog
import time
from common.pathUtils import pathUtils
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import *


class BasePage(object):

    def __init__(self, driver):
        self.logger = Mylog('BasePage.py').getlog()
        self.driver = driver

    def wait_eleVisible(self, locator, wait_times=10, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素定位，元组
        :param wait_times:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称
        :return:
        '''
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.logger.debug('{}:元素{}已可见，等待起始时间：{}，等待结束时间：{},等待耗时：{}'.format(doc, locator, start, end, wait_times))
        except:
            self.logger.exception('等待元素{}可见异常!'.format(locator))
            self.save_screenshot(doc)
            raise

    def get_element(self, locator, doc=''):

        try:
            if isinstance(locator, tuple):
                self.logger.info('{} 查找元素：{}'.format(doc, locator))
                return self.driver.find_element(*locator)
            elif isinstance(locator, str):
                self.logger.info('{} 查找元素：{}'.format(doc, locator))
                return self.driver.find_element_by_android_uiautomator(locator)
        except:
            self.logger.exception('{} 没有找到元素！！：{}'.format(doc, locator))
            self.save_screenshot(doc)

    def get_elements(self, locator, doc=''):
        try:
            self.logger.info('{} 查找元素：{}'.format(doc, locator))
            return self.driver.find_elements(*locator)
        except:
            self.logger.exception('{} 没有找到元素！！：{}'.format(doc, locator))
            self.save_screenshot(doc)

    def get_elements_text(self, locator, doc=''):
        """获取多个元素的值，返回list"""
        ments = []
        try:
            for ment in self.get_elements(locator):
                ments.append(ment.text)
            return ments
        except NoSuchElementException:
            self.save_screenshot(doc)
            self.logger.exception('获取多个元素的文本失败！！！')

    def click_element(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        try:
            ele.click()
            self.logger.info('{} 点击元素：{}'.format(doc, locator))
            time.sleep(1)
        except:
            self.save_screenshot(doc)
            self.logger.exception('元素点击操作失败！！！')
            raise

    def click_tap(self, tap):
        self.driver.tap([(tap[0], tap[1])], 200)

    def input_text(self, locator, text='', doc=''):
        ele = self.get_element(locator, doc)
        try:
            ele.send_keys(text)
            self.logger.info('{}:元素：{} 输入内容：{}'.format(doc, locator, text))
        except:
            self.logger.exception('元素输入操作失败！')
            self.save_screenshot(doc)
            raise

    def get_text(self, locator, doc=''):
        from appium.webdriver.common.mobileby import By
        if isinstance(locator[0], str):
            if locator[0] == 'By.id':
                locator = (By.ID, locator[1])
        ele = self.get_element(locator, doc)
        try:
            text = ele.text
            self.logger.info('元素：{}的文本内容为：{}'.format(locator, text))
            return text
        except:
            self.logger.exception('{}:获取元素：{}的文本内容失败！！'.format(doc, locator))
            self.save_screenshot(doc)
            raise

    def get_element_attribute(self, locator, attr, doc=''):
        ele = self.get_element(locator, doc)
        try:
            ele_attr = ele.get_attribute(attr)
            self.logger.info('元素：{}的属性 {}值为：{}'.format(locator, attr, ele_attr))
            return ele_attr
        except:
            self.logger.exception('{}:获取元素：{}的属性:{}失败！！'.format(doc, locator, attr))
            self.save_screenshot(doc)
            raise

    # def is_eleExist(self, locator, timeout=10, doc=''):
    #     """检查元素是否存在，不存在则抛出错误"""
    #     try:
    #         WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    #         self.logger.info('{} 秒内页面 {} 中存在元素：{}'.format(timeout, doc, locator))
    #         return True
    #     except TimeoutException:
    #         self.logger.error('{} 秒内页面 {} 中不存在元素：{}'.format(timeout, doc, locator))
    #         return False

    def swipe_find_ele(self, locator, action, direction='', method=1):
        """"下滑页面查找元素 直至可见过超时"""
        try:
            while True:
                if self.is_eleExist(locator, method):
                    if action.lower() == 'c':
                        self.click_element(locator)
                        return True
                    elif action.lower() == 's':
                        self.input_text(locator)
                        return True
                    elif action.lower() == 'is':
                        return self.is_eleExist(locator, method)
                    else:
                        return self.get_elements(locator)
                else:
                    self.swipe_direction(direction, 1, 9)
        except TimeoutException as e:
            self.logger.info('滑动页面查找元素超时！')

    def is_eleExist(self, locator, method=1):
        """检查元素是否存在，不存在则抛出错误"""

        try:
            if method == 1:
                a = self.driver.find_element(*locator)
                self.logger.info(a)
                return True
            elif method == 0:
                a = self.driver.find_element_by_android_uiautomator(locator)
                self.logger.info(a)
                return True
        except Exception:
            # self.logger.error('{}:该元素不存在!'.format(*locator))
            return False

    def swipe_direction(self, direction, num=1, distance=9):

        """
               屏幕滑动一次
               :param direction: 方向
                   up: 从下往上
                   down: 从上往下
                   left: 从右往左
                   right: 从左往右
               """
        # 控制上下滑动距离
        dic = {9: 0.75, 8: 0.7, 7: 0.7, 6: 0.65, 5: 0.6, 4: 0.55, 3: 0.5, 2: 0.45, 1: 0.4}
        if distance > 9:
            distances = 0.75
        else:
            distances = dic[distance]
        time.sleep(1)

        screen_size = self.driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]

        center_x = screen_width * 0.5
        # 屏幕顶部banner图片位置
        center_y = screen_height * 0.20

        top_x = center_x
        top_y = screen_height * 0.35
        down_x = center_x
        down_y = screen_height * distances
        left_x = screen_width * 0.1
        left_y = center_y
        right_x = screen_width * 0.9
        right_y = center_y

        for i in range(num):
            if direction == "up":
                self.driver.swipe(down_x, down_y, top_x, top_y, 2000)
            elif direction == "down":
                self.driver.swipe(top_x, top_y, down_x, down_y, 2000)
            elif direction == "left":
                self.driver.swipe(right_x, right_y, left_x, left_y, 2000)
            elif direction == "right":
                self.driver.swipe(left_x, left_y, right_x, right_y, 2000)
            else:
                raise Exception("请确定划动方向！ up、left、right、down")
            time.sleep(1)

        # """屏幕左划"""
        # size = self.driver.get_window_size()
        # start_x = size['width'] * 0.9
        # start_y = size['height'] * 0.5
        # end_x = size['width'] * 0.1
        # end_y = size['height'] * 0.5
        #
        # self.driver.swipe(start_x, start_y, end_x, end_y, 100)

    def get_size(self):
        """获取屏幕大小"""
        return self.driver.get_window_size()

    def get_toastMsg(self, string):
        loc = '//*[contains(@text,"{}")]'.format(string)
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, loc)))
            return self.driver.find_element_by_xpath(loc).text
        except:
            self.logger.exception('没有找到匹配的toast！！')
            raise

    def save_screenshot(self, doc='test'):
        file_path = pathUtils().get_screenShot_path(doc)
        try:
            self.driver.save_screenshot(file_path)
            self.logger.info('咔嚓 ->{}'.format(file_path))
        except:
            self.logger.exception('截图失败！！')

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
            self.sleep(0.5)

    @staticmethod
    def sleep(seconds=5.0):
        """强制等待"""
        time.sleep(seconds)

    def wait(self, seconds=20):
        """显示等待"""
        self.driver.implicitly_wait(seconds)
