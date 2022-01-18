# -*- coding: utf-8 -*-
#author：wzp
import unittest,os,sys
import multiprocessing
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.madb import m
from config.path import *
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
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
adb = ADB()


auto_setup(__file__, logdir=True)
#运行Testcase的主函数

def run_case(count):
    # 获取设备列表
    for _ in range(count):
        l.info("进入设备为{}的RunTestCase".format(m.getdevices()))
        if not os.path.exists(TestCasePath):
            l.error("测试用例需放到‘TestCase’文件目录下")

        devicesList = adb.devices()
        devicesNum = len(devicesList) > 1
        print("本次连接{}个设备，分别是".format(len(devicesList)), devicesList)
        assert_equal(devicesNum, True, "设备连接数量至少为2")

        for i in range(len(devicesList)):
            connect_device("android:///" + devicesList[i][0])
        # 通过GetPyList方法，取得目录里可测试的用例列表
            scriptList = File.GetPyList(TestCasePath)
            l.info("{}设备的待测用例为：{}".format(devicesList,scriptList))

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
        simple_report(__file__, logpath=True,logfile='{}/run/log/log.txt'.format(BASE_DIR),output='{}/subject.html'.format(Reportpath))
        l.info("测试报告在{}/subject.html查看".format(Reportpath))
        sendmail()





if __name__ == '__main__':
    p_list = []
    #控制执行次数
    for _ in range(1):
        p = multiprocessing.Process(target=run_case, args=(1,))
        p_list.append(p)
        print(p.name)

    for i in p_list:
        i.start()
        print(i.pid)

    for j in p_list:
        j.join()




































