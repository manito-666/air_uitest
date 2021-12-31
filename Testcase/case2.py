# -*- coding: utf-8 -*-

import inspect
import unittest
from util.log.mylog import l
from common.madb import m
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config.path import *

# 获取工程路径
pro_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".."
case_img=os.path.join(pro_path,'TestCaseImage','IH_project2')

def run_case(devices):
    l.debug("{}进入unittest".format(devices))
    package = m.get_packagename()
    l.info("打开package:{}".format(package))
    class Test1(unittest.TestCase):
        """用例描述"""
        @classmethod
        def setUpClass(cls):
            """ 这里放需要在所有用例执行前执行的部分"""
            l.info("Test2测试开始")

        def test1(self):
            self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            start_app(package)
            sleep(3)
            wait(Template(r"{}/tpl1640068688954.png".format(case_img)))
            sleep(2)
            touch(Template(r"{}/tpl1640068688954.png".format(case_img)))
            sleep(2)
            l.info("游客登录")
            touch(Template(r"{}/tpl1639968941165.png".format(case_img)))
            sleep(2)
            l.info("进入游戏")
            wait(Template(r"{}/tpl1639968982108.png".format(case_img)))
            sleep(2)
            touch(Template(r"{}/tpl1639968982108.png".format(case_img)))
            sleep(2)
            if assert_exists(Template(r"{}/tpl1639969036102.png".format(case_img))):
                l.info("查看游戏ID成功")
                sleep(2)
            else:
                l.info("测试失败")
        @classmethod
        def tearDownClass(cls):
            """这里放需要在所有用例后执行的部分"""
            l.info("测试结束")
            stop_app(package)

    srcSuite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    # srcSuite =Test1("test1")
    return srcSuite


# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)