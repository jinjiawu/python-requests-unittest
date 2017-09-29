# -*- coding:utf-8 -*-
from comments.read_xls import Read_xls_file
from comments.log import Logger
import unittest
import requests

logger = Logger(logger='water_repoter').getlog()

class Get_water_repoter(unittest.TestCase):
    '''
    获取水质报告
    '''
    def setUp(self):
        #获取xls表中的测试数据
        self.file_contains = Read_xls_file('water.xlsx').get_xls()[0]
        self.url = self.file_contains[1]
        self.data = eval(self.file_contains[2])#eval可以将str转换成dict


    def tearDown(self):
        logger.info('水质报告获取测试结束')

    def test_get_weather(self):
        result = requests.get(self.url,params=self.data)
        self.assertEqual(result.status_code,200,msg='status_code error')

if __name__ == '__main__':
    unittest.main()