# -*- coding: utf-8 -*-
# 读取/写入配置文件
import configparser


con = configparser.ConfigParser()

# 获取项目名称
def getProName(path, key):
    con.read(path)
    result = con.get("project", key)
    return result

# 读取TestCaseforDevice 节点下的键值
def getTestCase(path, pro, device=""):
    if device != "":
        con.read(path)
        result = con.get("{}".format(pro), device)
        case_list = result.split(",")
        return case_list
    else:
        return []

# 获取Email key值
def getEmail(path,key):
    con.read(path)
    result = con.get("Email", key)
    return result

# 获取android key值
def getAndroid(path, key):
    con.read(path)
    result = con.get("Android", key)
    return result
def getBasicConfig(path, key):
    con.read(path)
    result = con.get("basic_config", key)
    return result


# 重新回写配置文件
def setValue(configpath, key, value):
    if key != "" and value != "":
        con.set("Android", key, value)
        con.write(open(configpath, "w"))

