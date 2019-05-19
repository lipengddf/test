#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
from appium import webdriver
from time import sleep
import unittest
# 测试脚本与appium服务器进行连接的参数数据
class DS(unittest.TestCase):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "5cbca868",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "true"
    }

    def setUp(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(5.0)
        return self.dr
    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
    def longin(self,phone,password):
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18236910059')
        sleep(5)
        #向密码输入框内输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a18236910059')
        sleep(5)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)


        #清空账号
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
        # sleep(3)
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18236910059')
        # sleep(3)
        # 向密码输入框内输入密码
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').clear()   #清空密码
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a18236910058')
        # sleep(3)
        # self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        # sleep(3)

        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').clear()  # 清空密码
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a18236910059')
        # sleep(3)
        # self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        # sleep(10)
        # # 清空数据
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()

    #app退出登录
    def logout(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        a = self.dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.RelativeLayout')
        print(a)
        sleep(3)
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
    def close_app(self):
        self.dr.quit()
if __name__ == '__main__':
    go = DS()#创建一个DS类
    print(go.setUp())
    go.tiao_zhuan()
    go.longin('18236910059','a18236910059')
    go.tui()
    go.close_app()

