# -*- coding: utf-8 -*-

import inspect,sys
import unittest
from util.log.mylog import l
from common.madb import m
from airtest.core.api import *
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config.path import *

# 获取工程路径
pro_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".."
case_img=os.path.join(pro_path,'TestCaseImage','IH_project1')

def run_case(devices):
    l.debug("{}进入unittest".format(devices))
    package = m.get_packagename()
    l.info("打开package:{}".format(package))


    class Test1(unittest.TestCase):
        """用例描述"""
        @classmethod
        def setUpClass(cls):
            """ 这里放需要在所有用例执行前执行的部分"""
            l.info("Test1测试开始")

        def test1(self):
            self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            start_app(package)
            sleep(3)
            wait(Template(r"{}/tpl1641439963719.png".format(case_img)))
            sleep(2)
            touch(Template(r"{}/tpl1641439963719.png".format(case_img)))
            sleep(2)
            l.info("游客登录")
            touch(Template(r"{}/tpl1642402804463.png".format(case_img,times=2,duration=0.01)))
            sleep(3)
            l.info("点击进入游戏")
            touch(Template(r"{}/tpl1642403244950.png".format(case_img)))
            sleep(2)
            l.info("关闭新手签到")
            wait(Template(r"{}/tpl1641440148357.png".format(case_img)))
            touch(Template(r"{}/tpl1641440148357.png".format(case_img)))
            sleep(2)
            l.info("点击消息")
            touch(Template(r"{}/tpl1641440166490.png".format(case_img)))
            if assert_exists(Template(r"{}/tpl1640070352186.png".format(case_img))):
                l.info("查看游戏公告成功")
            else:
                l.info("测试失败")
            sleep(2)
        @classmethod
        def tearDownClass(cls):
            """这里放需要在所有用例后执行的部分"""
            l.info("测试结束")
            stop_app(package)

    srcSuite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    return srcSuite




# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)