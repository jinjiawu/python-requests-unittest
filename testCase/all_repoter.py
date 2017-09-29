# -*- coding:utf-8 -*-
from comments.log import Logger
from comments.read_xls import Read_xls_file
import unittest
import requests
import os.path
import xlwt

logger = Logger(logger='all_repoter').getlog()

class Get_All_repoter(unittest.TestCase):
    '''
    获取所有的报告
    '''

    def setUp(self):
        #所有接口名字存放
        self.names = []
        #所有接口地址存放
        self.urls = []
        #所有接口数据存放
        self.datas = []
        #所有返回的状态码存放
        self.all_codes = []
        #所有测试结果存放pass或者fail
        self.all_result = []
        #把表中所有的数据都读出来
        self.file_contains = Read_xls_file('all.xlsx').get_xls()
        for i in self.file_contains:
            self.names.append(i[0])
            self.urls.append(i[1])
            self.datas.append(i[2])
            logger.info('%s信息获取完毕'%i[0])

    def tearDown(self):
        pass

    def est_get_all(self):
        for n in range(len(self.urls)):
            results = requests.get(self.urls[n],params=eval(self.datas[n]))
            self.assertEqual(results.status_code,200,msg='code error')
            self.all_codes.append(results.status_code)#将所有返回的状态码存进all_codes里面
            if results.status_code == 200:
                self.all_result.append('pass')
            else:
                self.all_result.append('fail')
            print(results.json())

    def test_write_to_excel(self):
        all_files = list(zip(self.names,self.urls,self.datas))
        file_path = os.path.dirname(os.path.abspath('.'))+'/repoter/repoter.xls'
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('All_repoter')#sheet的名称为All_repoter


if __name__ == '__main__':
    unittest.main()