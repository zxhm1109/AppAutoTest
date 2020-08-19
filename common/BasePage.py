#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/31 11:54
# @File      : BasePage.py
# @desc      :

import logging
import time
from common import path_conf
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素定位，元组
        :param wait_times:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称
        :return:
        '''
        logging.info('等待元素{}可见'.format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info('{}:元素{}已可见，等待起始时间：{}，等待结束时间：{},等待耗时：{}'.format(doc, locator, start, end, wait_times))
        except:
            logging.exception('等待元素可见异常!')
            self.save_screenshot(doc)
            raise

    def get_element(self, locator, doc=''):
        logging.info('{} 查找元素：{}'.format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败！！！')
            self.save_screenshot(doc)
            raise

    def click_element(self, locator, doc=''):
        ele = self.get_element(*locator, doc)
        logging.info('{} 点击元素：{}'.format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception('元素点击操作失败！！！')
            self.save_screenshot(doc)
            raise

    def input_text(self, locator, text, doc=''):
        ele = self.get_element(locator, doc)
        logging.info('{}:元素：{} 输入内容：{}'.format(doc, locator, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception('元素输入操作失败！')
            self.save_screenshot(doc)
            raise

    def get_text(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        logging.info('{}:获取元素：{}的文本内容'.format(doc, locator))
        try:
            text = ele.text
            logging.info('元素：{}的文本内容为：{}'.format(locator, text))
            return text
        except:
            logging.exception('获取元素文本内容失败！！')
            self.save_screenshot(doc)
            raise

    def get_element_attribute(self, locator, attr, doc=''):
        ele = self.get_element(locator, doc)
        logging.info('{}:获取元素：{}的属性:{}'.format(doc, locator, attr))
        try:
            ele_attr = ele.get_attribute(attr)
            logging.info('元素：{}的属性 {}值为：{}'.format(locator, attr, ele_attr))
            return ele_attr
        except:
            logging.exception('获取元素的属性失败！！')
            self.save_screenshot(doc)
            raise

    def is_eleExist(self, locator, timeout=10, doc=''):
        logging.info('在页面{}中是否存在元素：{}'.format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info('{} 秒内页面 {} 中存在元素：{}'.format(timeout, doc, locator))
            return True
        except:
            logging.exception('{} 秒内页面 {} 中不存在元素：{}'.format(timeout, doc, locator))
            return False

    def swipe_left(self):
        """屏幕左划"""
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.5
        end_x = size['width'] * 0.1
        end_y = size['height'] * 0.5

        self.driver.swipe(start_x, start_y, end_x, end_y, 100)

    def get_size(self):
        """获取屏幕大小"""
        return self.driver.get_window_size()

    def get_toastMsg(self, string):
        loc = '//*[contains(@text,"{}")]'.format(string)
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, loc)))
            return self.driver.find_element_by_xpath(loc).text
        except:
            logging.exception('没有找到匹配的toast！！')
            raise

    def save_screenshot(self, doc):
        file_path = path_conf.screenShot_path + '/{}_{}.png'.format(doc, time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()))
        try:
            self.driver.save_screenshot(file_path)
            logging.info('咔嚓 ->{}'.format(file_path))
        except:
            logging.exception('截图失败！！')
