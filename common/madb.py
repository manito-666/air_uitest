# -*- coding: utf-8 -*-
#配置公共方法
import json
import os,sys,queue
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
import inspect,requests,re
from airtest.utils.apkparser import APK
from util.log.mylog import l
from common import Config
from config.path import *
from airtest.core.android.android import *
adb = ADB().adb_path
q = queue.Queue()

class Madb:
    def __init__(self):
        # 获取当前文件的上层路径
        self._parentPath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
        # 获取当前项目的根路径
        self._rootPath = os.path.abspath(os.path.dirname(self._parentPath) + os.path.sep + ".")
        self._configPath = self._rootPath + "/config/config.ini"
        self._pro_name = Config.getProName(self._configPath, "prj_name")
        l.info(self._pro_name)
        self._devicesList = Config.getAndroid(self._configPath, "deviceslist")
        self._apppackage=Config.getAndroid(self._configPath, "apppackage")
        self.testCasePath=TestCasePath
        self._packagePath = Config.getAndroid(self._configPath, "apkpath")
        self._auto_install_package = Config.getAndroid(self._configPath, "auto_install_package")
        self._timeout_of_startapp = int(Config.getBasicConfig(self._configPath, "timeout_of_startapp"))
    # 读取实时的设备连接
    def getdevices(self):
        deviceslist = []
        for devices in os.popen(adb + " devices"):
            if "\t" in devices:
                if devices.find("emulator") < 0:
                    if devices.split("\t")[1] == "device\n":
                        devices = devices.split("\t")[0]
                        deviceslist.append(devices)
                        # l.info("设备{}被添加到deviceslist中".format(devices))
                        #读取设备后添加到配置文件中
                        Config.setValue(self._configPath,"deviceslist",devices)
        return deviceslist

    # 启动APP
    def StartApp(self):
        devices = self.getdevices()
        l.info("{}设备进入StartAPP函数".format(devices))

    # 判断给定设备的安卓版本号
    def get_androidversion(self):
        command = adb + " -s {} shell getprop ro.build.version.release".format(self.getdevices()[0])
        version = os.popen(command).read()
        l.info("设备系统为{}".format(version))

    # 判断给定设备的手机型号
    def get_androidmodel(self):
        command = adb + " -s {} shell getprop ro.product.model".format(self.getdevices()[0])
        brand = os.popen(command).read()
        l.info("设备的手机型号为{}".format(brand))

    def get_androidsize(self):
        size_str = os.popen('adb shell wm size').read()
        m = re.search(r'(\d+)x(\d+)', size_str)
        l.info("设备分辨率为：{height}x{width}".format(height=m.group(2), width=m.group(1)))



    #获取包名
    def get_packagename(self):
        return self._apppackage

    def auto_install_package(self):
        return self._auto_install_package

    #获取包本地路径
    def get_apkpath(self):
        return self._packagePath

    # 获取启动app的延时时间
    def get_timeout_of_startapp(self):
        return self._timeout_of_startapp

    def AppInstall(self):
        devices = self.getdevices()
        apkpath = self.get_apkpath()
        package = self.get_packagename()
        l.info("设备{}开始进行自动安装".format(devices))
        auto_install_package = self.auto_install_package()
        auto_install_package = True if auto_install_package == "1" else False

        if not os.path.exists(apkpath):
            url='http://inner-cdn.dhgames.cn:22345/ih/package/com.dhgames.ih.dev.android/ih_develop-0.90.0.apk'
            r = requests.get(url)
            with open(apkpath, "wb") as code:
                try:
                    code.write(r.content)
                except Exception:
                    l.error('下载失败')
                else:
                    if os.path.exists(apkpath):
                        l.info('下载成功')
        try:
            time.sleep(self.get_timeout_of_startapp())
            command = adb+ " -s " + str(devices[0]) + " install -r " + apkpath
            l.info("正在{}上安装{},安装命令为：{}".format(devices[0], package, command))
            if auto_install_package:
                os.system(command)
            if self.isinstalled():
                l.info("{}上安装成功，退出AppInstall线程".format(devices))
                # 将线程函数的返回值放入queue
                q.put("Install Success")
                return True
            else:
                l.error("{}上安装未成功".format(devices))
                q.put("Install Fail")
                return False
        except Exception as e:
            l.error("{}上安装异常".format(devices))
            l.error(e)
            q.put("Install Fail")

    # 判断给定设备里是否已经安装了指定apk
    def isinstalled(self):
        devices = self.getdevices()
        package = self.get_packagename()
        command = adb + " -s {} shell pm list package".format(devices[0])
        l.info(command)
        commandresult = os.popen(command)

        l.info("设备{}进入检测是否有安装包，package={}".format(devices, package))
        for pkg in commandresult:
            if "package:" + package in pkg:
                l.info("在{}上发现已安装{}".format(devices, package))
                return True
        l.info("在{}上没找到包{}".format(devices, package))
        return False

    def get_skip_pushapk2devices(self):
        return self._skip_pushapk2devices


m=Madb()
