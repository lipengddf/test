#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
import yaml
from appium import webdriver
from time import sleep
with open(r'C:\Users\admin\PycharmProjects\untitled\src\element\qaz.yaml','r',encoding='utf-8') as fb:
    # a = yaml.load(fb) 使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data = yaml.load(fb,Loader=yaml.CFullLoader)
    print(item_data)
    print(type(item_data))
    print(item_data['three']['wx_id'])
    def wx(driver):
        sleep(2)
        text1 = driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
        return text1

    def qq(driver):
        sleep(2)
        # driver = dr
        text2 = driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
        return text2


    def wb(driver):
        sleep(2)
        # driver = dr
        text3 = driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
        return text3


    def pwd(driver):
        sleep(2)
        # driver = dr
        text4 = driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
        return text4

# def foo(driver):
#     # dr = driver
#     text = driver.find_element_by_id('com.qk.butterfly:id_login_wx').find_element_by_class_name(
#         'android.widget.TextView').text
#     #   weixin
#     return text
# foo(dr)
