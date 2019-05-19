#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
from appium import webdriver
from time import sleep
import unittest
from src.until.denglu import DS
class tuichu(object):

    a = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "5cbca868",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    sleep(10)
    def tui(self):
        a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        print(a)
        a[3].click()
        #模拟人工上划    1）、获取当前平魔分辨率
        size = self.dr.get_window_size()
        x1 = size['width'] * 0.5  # x坐标 50
        y1 = size['height'] * 0.25  # 起始y坐标 50
        y2 = size['height'] * 0.75  # 150
        for i in range(2):
            self.dr.swipe(x1, y2, x1, y1)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        sleep(1)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
        sleep(1)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
        sleep(1)
DS().setUp()
DS().tiao_zhuan()
DS().longin('18236910059','a18236910059')
DS().logout()
DS().close_app()
tuichu().tui()