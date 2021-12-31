import  os
import  datetime
# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, 'util','log')

# 截图文件
SCRE_DIR = os.path.join(BASE_DIR, 'util','screen')

#当前时间
NOW_TIME = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# 运行文件
RUN_DIR = os.path.join(BASE_DIR, 'run','pro_main.py')

#报告目录
Reportpath=os.path.join(BASE_DIR,'util','report')

#测试用例目录
TestCasePath=os.path.join(BASE_DIR,'Testcase')

