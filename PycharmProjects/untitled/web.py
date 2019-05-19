#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
# from  selenium import webdriver
# from time import sleep
# #定义打开的浏览器
# dr = webdriver.Firefox()
# sleep(2)
# #请求网页
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.get('http://www.jd.com')
# sleep(2)
#回到上一次打开的网页
# dr.back()
# sleep(2)
#前进
# dr.forward()
#关闭浏览器
# dr.quit()
#获取网页标题,一般用作断言，判断请求到的标题是否符合预期结果
# print(dr.title)
#获取请求的网址
# print(dr.current_url)
#设置浏览器窗口大小
# dr.set_window_size(400,400)
#设置浏览器窗口的位置
# dr.set_window_position(400,400)
#最大化浏览器
# dr.maximize_window()
# sleep(3)
#最小化浏览器
# dr.minimize_window()
# sleep(2)


#1 、id  定位
# dr.find_element_by_id('kw').send_keys('python')
# dr.find_element_by_id('su').click()
#2、class 为了区分跟python中的class，class_name
#单个定位的时候保证class的值是唯一的
# dr.find_element_by_class_name('manv').click()
#3、name 通过name定位
# dr.find_element_by_name('wd').send_keys('python')
#4、link_text文本定位
# dr.find_element_by_link_text('视频').click()
#5、partial link text  模糊文本定位
# dr.find_element_by_link_text('hao').click()
#6、tag_name  定位  通过标签页的名称
# dr.find_element_by_tag_name('')
#7、xpath  定位  路径定位
#路径标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').click()
#8、css  定位
# dr.find_element_by_css_selector('#kw').click()
#动作：1、send_keys()  输入     2、click()   点击      3、clear()  清除     4、text   文本



# from  selenium import webdriver
# from time import sleep
# import os
# # #定义打开的浏览器
# dr = webdriver.Firefox()
# # #请求网页
# dr.get('https://qzone.qq.com/')
# sleep(2)
# #自动登录QQ空间
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('319808789')
# sleep(2)
# dr.find_element_by_id('p').send_keys('ai319808789')
# sleep(2)
# dr.find_element_by_css_selector('#login_button').click()
# sleep(2)
# #定位到退出的按钮
# dr.find_element_by_id('tb_logout').click()
# sleep(2)
#切换到alter上去，自动点击确定
# we = dr.switch_to.alert()
# #获取alter上面的文本
# print(we.text)
# #点击确定
# we.accept()
#点击取消
# we.dismiss()
#点击退出的时候会弹出框   叫alert
#定位一组，定位多个数据
# ww = dr.find_element_by_id('su')
#层级定位：先定位一个顶层元素，在定位这个元素下面的元素
# dr.get('https://www.ctrip.com')
# sleep(2)
#层级定位，多用于复杂的定位场景
# ww = dr.find_element_by_id('searchHotelLevelSelect').click().find_elements_by_class_name('option')

# from  selenium import webdriver
# from time import sleep
# #定义打开的浏览器
# dr = webdriver.Firefox()
# #请求网页
# dr.get('file:///C:/Users/admin/Desktop/abc.html')
# sleep(2)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
#将控制器切换至弹出框
# ww = dr.switch_to.alert()
#获取弹出框上的文本
# print(ww.text)
#点击确定
# ww.accept()
#点击取消
# ww.dismiss()
#输入数据
# ww.send_keys('你好吗？')




# from  selenium import webdriver
# from time import sleep
# import os
# # #定义打开的浏览器
# dr = webdriver.Firefox()
# # #请求网页
# dr.get('https://qzone.qq.com/')
# sleep(2)
# #自动登录QQ空间
# dr.switch_to.frame('login_frame')
# sleep(2)
# #切换到框架 id ，name
# #先定义到框架
# w = dr.find_element_by_xpath('//*[@id="login"]').click()
# dr.switch_to.frame(w)
# sleep(2)
# dr.switch_to.parent_frame()
# sleep(2)
# #退出框架,退出到最初的页面
# # dr.switch_to_default_content()
# dr.find_element_by_xpath('html/body/div[3]/div/div/div[1]/div[1]/a[2]/i').click()
# #iframe    网页框架



from  selenium import webdriver
from time import sleep
# import os
# #定义打开的浏览器
dr = webdriver.Firefox()
# #请求网页
dr.get('https://www.douban.com/')# 1号窗口
sleep(2)
#获取第一个窗口的标识（句柄）
print(dr.current_window_handle)
# 2号窗口
dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
#获取所有窗口的标识
ww = dr.window_handles
sleep(2)
# print(ww)
dr.switch_to.window(ww[-1])
print(dr.title)

#切换窗口
#浏览器本身是无法决定什么时候打开哪一个窗口
#按照窗口打开的顺序给窗口标号（唯一标识这个窗口的字符串）
# dr.switch_to_window()