# -*- coding: gbk -*-
import configparser
import os
class Page_config(object):
    def __init__(self):
        # os.path.dirname 去掉文件名 返回目录
        # os.path.realpath(__file__)  范围当前文件目录包括文件名
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        ZHEN_DIR = os.path.join(BASE_DIR, 'config.ini')
        self.file = ZHEN_DIR
        self.config = configparser.ConfigParser()
        self.config.read(self.file)
    # 获得所有section 列表返回
    def getAllSections(self):
        return self.config.sections()
    # 获得所有option 列表返回
    def getAllOptions(self, section):
        return self.config.options(section)
    # 获取指定option 的值， 以字典格式返回
    def getOnesection(self,section,option):
        try:
            locator =self.config.get(section,option)
            if option in self.config.options(section):
                locator = {option:locator}
                # locator = dict(self.config.items())
            return locator
        except configparser.NoOptionError as e:
            return  e
            # return 'error: No option "{}" in section: "{}"'.format(option, section)

page = Page_config()

