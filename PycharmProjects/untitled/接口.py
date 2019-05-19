#!/usr/bin/python
# -*- coding:utf-8 -*-
#! the author lipeng
import requests
from jiekou_kuang.report import HTMLTestRunner
import unittest
import xlrd
f=xlrd.open_workbook('a.xls')
sheet=f.sheets()[0]
row_1=sheet.nrows
class Denglu(unittest.TestCase):
        def dizhi(self,user,password):
            url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
            payload = '{"phone":"%s","password":"%s",' \
                      '"zone":"86","loginType":0,"isAuto":0,' \
                      '"deviceId":"ec:89:14:54:93:007"}'%(user,password)
            headers = {
                'Content-Type': "application/json",
                'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
                'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
                'Language': "zh_CN",
                'APIVersion': "3.0",
                'User-Agent': "PostmanRuntime/7.11.0",
                'Accept': "*/*",
                'Cache-Control': "no-cache",
                'Postman-Token': "90834b61-e0c4-44ee-9652-a87b698b93cd,ed8a20cd-d86c-4ad8-a8e5-26f5e8d2501c",
                'Host': "120.132.8.33:9000",
                'accept-encoding': "gzip, deflate",
                'content-length': "150",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
                }
            response = requests.request("POST", url, data=payload, headers=headers)
            res = response.json()
            return res
        def setUp(self):
            print('开始')
        def tearDown(self):
            print('结束')
        def test_1(self):
            qq = self.dizhi(int(sheet.cell(1,0).value),int(sheet.cell(1,1).value))
            self.assertEqual(qq['code'],0)
        def test_2(self):
            for i in range(2,row_1):
                ww = self.dizhi(int(sheet.cell(i, 0).value), int(sheet.cell(i, 1).value))
                self.assertNotEqual(ww['code'],0)
if __name__ == '__main__':
    unittest.main()
    # suit=unittest.TestSuite()     #创建一个测试套件
    # suit.addTest(Denglu('test_1'))    #将测试用例添加到测试套件中
    # suit.addTest(Denglu('test_2'))
    # suit.addTest(unittest.makeSuite(Denglu))    #将Denglu类中所有以test开头的函数都添加到测试套件中
    # ff=open('abc.html','wb')     #打开一个空文件
    # runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='小白', description='结果如下')#定义测试报告的信息
    # runner.run(suit)    #执、行测试套件
    # ff.close()
# a,b = 0,100
# while b > 0:
#     a += b
#     b -= 1
#     print(a)