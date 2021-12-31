# -*- coding: gbk -*-
import configparser
import os
class Page_config(object):
    def __init__(self):
        # os.path.dirname ȥ���ļ��� ����Ŀ¼
        # os.path.realpath(__file__)  ��Χ��ǰ�ļ�Ŀ¼�����ļ���
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        ZHEN_DIR = os.path.join(BASE_DIR, 'config.ini')
        self.file = ZHEN_DIR
        self.config = configparser.ConfigParser()
        self.config.read(self.file)
    # �������section �б���
    def getAllSections(self):
        return self.config.sections()
    # �������option �б���
    def getAllOptions(self, section):
        return self.config.options(section)
    # ��ȡָ��option ��ֵ�� ���ֵ��ʽ����
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

