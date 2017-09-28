# -*- coding:utf-8 -*-
from comments.log import Logger
from comments.read_xls import Read_xls_file
import unittest
import requests

logger = Logger(logger='weather_repoter').getlog()

class Get_weather_repoter(unittest.TestCase):
    '''
    获取天气预报
    '''
    def setUp(self):
        #获取xls表中的测试数据
        self.file_contains = Read_xls_file('weather.xlsx').get_xls()[0]
        self.url = self.file_contains[1]
        self.data = self.file_contains[2]
        print(type(self.data))

    def tearDown(self):
        logger.info('天气预报测试结束')

    def test_get_weather(self):
        #result = requests.get(self.url,params=self.data)
        result = requests.get('http://v.juhe.cn/weather/index',
                              params={'format':2,'cityname':'无锡','key':'da77a5dc91e578704ffe77c589d18006'})
        print(result.json())

if __name__ == '__main__':
    unittest.main()