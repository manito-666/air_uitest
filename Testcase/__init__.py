# -*- coding: utf-8 -*-

import inspect
import os

# 自动引入当前文件夹下所有py文件
from util import File

Path = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
pyList = File.GetPyList(Path)

__all__ = pyList
