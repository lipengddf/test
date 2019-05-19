#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
from appium import webdriver
from time import sleep
import unittest
# 测试脚本与appium服务器进行连接的参数数据
class ds(unittest.TestCase):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "5cbca868",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "true"
    }
    # def setUp(self):
    #建立连接函数
        # self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
        # sleep(5.0)
    #所有的用例执行之前，跑一次，只跑一次
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
        sleep(15.0)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    #断言微信文字是否存在
    def test_1(self):
        text = self.dr.find_element_by_id('com.qk.butterfly:id_login_wx').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text,'微信')
        print(text)
    def test_2(self):
        text2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text2,'微博')
        print(text2)
    def test_3(self):
        text3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text3,'QQ')
        print(text3)
    def test_4(self):
        text4 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
        print(text4)
        self.assertEqual(text4,'密码')
    #关闭APP的函数
    def close_app(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()