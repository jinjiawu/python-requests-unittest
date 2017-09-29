# -*- coding:utf-8 -*-
import os.path
import xlrd
from comments.log import Logger

logger = Logger(logger='read_xls').getlog()

class Read_xls_file():

    def __init__(self,data_name):
        self.dir = os.path.dirname(os.path.abspath('.'))#项目的根目录
        self.file_path = self.dir+'/testData/%s'%data_name#根据文档名获取测试数据路径


    def get_xls(self):
        #读取xls文件
        bk = xlrd.open_workbook(self.file_path)
        logger.info("读取xls文件")

        #获取第一个页签内容
        sh = bk.sheet_by_name('Sheet1')
        logger.info("读取第一个页签的内容")

        #获取行数
        nrows = sh.nrows
        logger.info("获取行数")

        #获取列数
        nclos = sh.ncols
        logger.info("获取列数")

        #获取各行数据
        row_list = []
        for i in range(1,nrows):
            row_data = sh.row_values(i)
            row_list.append(row_data)
        logger.info("获取数据并存到列表中")

        #返回读取到的测试数据
        return row_list

