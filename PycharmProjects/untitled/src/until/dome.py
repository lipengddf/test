#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
#第一步导入appium模块中的webdriver类
from appium import webdriver
from time import sleep
#面向过程
#测试脚本与appium服务器进行连接的参数数据
d = {
  "device": "android",
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "5cbca868",
  "appPackage": "com.qk.butterfly",
  "appActivity": ".main.LauncherActivity",
  "noReset": "true"
}
#写死的 http://127.0.0.1:4732/wd/hub
#测试脚本是appium服务器与手机建立连接的过程
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
sleep(5.0)
#元素是id，就使用id定位方法
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
#获取微信的文字
#元素的多级定位
#先定位上一级，再定位下面的元素，找class属性
# text = dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# print(text)
# text2 = dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# print(text2)
# text3 = dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# print(text3)
# text4 = dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# print(text4)
#插入等待时间,休眠时间
sleep(5.0)
#send_keys()输入的是字符串
#什么时候可以用send_keys？
#1、向手机的输入框内输入数据的时候    #2、clickable --->>true     # 3 enabled ---》 true    # 4 foucsable --》 true
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(5.0)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18236910059')
#向密码输入框内输入密码
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a18236910059')
sleep(5.0)
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#查看登录后的效果
sleep(10)
#退出APP，包括后台进程也关掉
dr.quit()