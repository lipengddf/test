#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
from src.func.func_2 import wx,qq,wb,pwd
from appium import webdriver
import unittest
import HTMLTestRunner
from time import sleep
from src.文件 import REPORT_DIR
from src.testcase.rizhi import get_logger

#给日志一个变量
g = get_logger(name='testcase_3.py')
#测试脚本
class Text(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #建立连接

        a = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "5cbca868",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "True"
        }
        #app建立连接
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
        sleep(10)
        g.info('app建立连接完成')
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        g.info('app关闭')
    #测试用例的代码
    def test_1(self):
        #验证微信的用例
        text = wx(self.dr)
        self.assertEqual(text, '微信')
    def test_2(self):
        text = qq(self.dr)
        self.assertEqual(text, 'QQ')
    def test_3(self):
        text = wb(self.dr)
        self.assertEqual(text, '微博')
    def test_4(self):
        text = pwd(self.dr)
        #断言
        self.assertEqual(text,'密码')



#运行测试脚本、生成测试报告
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Text('test_1'))
    suite.addTest(Text('test_2'))
    suite.addTest(Text('test_3'))
    suite.addTest(Text('test_4'))
    #将测试结果写入html文件中
    #生成测试报告路径

    #将路径写死
    # r_path = r'C:\Users\admin\PycharmProjects\untitled\src\testcase\HTMLReport.html'

    #将路径写活
    r_path_1 = REPORT_DIR + 'HTMLReport.html'

    with open('HTMLReport.html','wb') as fb:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                title='测试报告',
                                # tester='李鹏'
                                description='报告的描述信息',
                                verbosity=2)
        #verbosity默认是0,  2使控制台输出的信息更详细
        #运行测试用例
        runner.run(suite)