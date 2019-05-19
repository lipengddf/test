#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
from appium import webdriver
import time
a = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "5cbca868",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": ".main.MainActivity",
        "noReset": "True"
    }
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
while True:
    time.sleep(2)
    size = dr.get_window_size()
    x1 = size['width'] * 0.5
    y1 = size['height'] * 0.25
    y2 = size['height'] * 0.75
    for i in range(2):
        dr.swipe(x1, y2, x1, y1)
    time.sleep(10)