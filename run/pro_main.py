# -*- coding: utf-8 -*-
#author：wzp
import unittest,os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.madb import m
from config.path import *
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from airtest.core.api import *
from util.log.mylog import l
from Testcase import *
from util import File
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.send_email import sendmail
from airtest.report.report import simple_report
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from airtest.core.android.adb import ADB
adb = ADB()


auto_setup(__file__, logdir=True)
#运行Testcase的主函数
def RunTestCase():
    # 获取设备列表
    l.info("进入设备为{}的RunTestCase".format(m.getdevices()))
    m.get_androidversion()
    m.get_androidmodel()
    # m.get_androidsize()
    if not os.path.exists(TestCasePath):
        l.error("测试用例需放到‘TestCase’文件目录下")
    TestList=m.getdevices()
    # 通过GetPyList方法，取得目录里可测试的用例列表
    scriptList = File.GetPyList(TestCasePath)
    l.info("{}设备的待测用例为：{}".format(TestList,scriptList))
    # 初始化测试套件
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    # 初始化poco
    poco = AndroidUiautomationPoco().device
    for i in range(len(scriptList)):
        fileName = scriptList[i]
        l.debug("fileName={}.py".format(fileName))
        if fileName in scriptList:
            result = globals()[fileName].run_case(m.getdevices())
            # 根据result类型判断调试单个方法or全部方法
            if isinstance(result, unittest.suite.TestSuite):
                suite.addTests(result)
            else:
                suite.addTest(result)
    runner.run(suite)
    # simple_report(__file__, logpath=True,logfile='{}/run/log/log.txt'.format(BASE_DIR),output='{}/subject.html'.format(Reportpath))
    # l.info("测试报告在{}/subject.html查看".format(Reportpath))
    # sendmail()




if __name__ == '__main__':
    RunTestCase()




































