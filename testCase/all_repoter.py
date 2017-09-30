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
    @classmethod
    def setUpClass(self):
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
        #测试报表的title
        self.titles = ('接口名','接口地址','接口数据','返回值','测试结果')
        #把表中所有的数据都读出来
        self.file_contains = Read_xls_file('all.xlsx').get_xls()
        for i in self.file_contains:
            self.names.append(i[0])
            self.urls.append(i[1])
            self.datas.append(i[2])
            logger.info('%s信息获取完毕'%i[0])

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_all(self):
        for n in range(len(self.urls)):
            results = requests.get(self.urls[n],params=eval(self.datas[n]))
            try:
                self.assertEqual(results.json()['resultcode'],'200',msg='code error')
            except AssertionError as A:
                logger.info(A)
            self.all_codes.append(results.json()['resultcode'])#将所有返回的状态码存进all_codes里面
            if results.json()['resultcode'] == '200':
                self.all_result.append('pass')
            else:
                self.all_result.append('fail')
        #将所有数据存放在all_files中
        all_files = list(zip(self.names,self.urls,self.datas,self.all_codes,self.all_result))
        all_files.insert(0,self.titles)
        return all_files

    def test_write_to_excel(self):
        all_files = self.test_get_all()
        file_path = os.path.dirname(os.path.abspath('.'))+'/repoter/repoter.xls'
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('All_repoter')#sheet的名称为All_repoter

        #单元格的格式
        pass_style = 'pattern:pattern solid,fore_colour green;font: bold on;'#背景颜色绿色，粗体字
        pass_header_style = xlwt.easyxf(pass_style)

        fail_style = 'pattern:pattern solid,fore_colour red;font: bold on;'#背景颜色红色，粗体字
        fail_header_style = xlwt.easyxf(fail_style)

        #获取行数
        row_count = len(all_files)
        #获取列数
        col_count = len(all_files[0])

        for row in range(row_count):
            for col in range(col_count):
                if all_files[row][col] == 'pass':#如果测试通过就标绿色
                    sheet.write(row, col, all_files[row][col], pass_header_style)
                elif all_files[row][col] == 'fail':#如果测试失败就标红色
                    sheet.write(row, col, all_files[row][col],fail_header_style)
                else:
                    sheet.write(row, col, all_files[row][col])
        wb.save(file_path)


if __name__ == '__main__':
    unittest.main()