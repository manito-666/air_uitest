# coding:utf-8
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.path import Reportpath
from util.log.mylog import l
from common.Config import getEmail as R

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
path=os.path.join(base_path,'config','config.ini')

# 163的用户名和授权密码
send_name =R(path,'name')
send_pwd = R(path,'pwd')
receive = R(path,'addr')
subject=R(path,'subject')
text=R(path,'email_text')

def sendmail():
    #获取报告目录下最新的测试报告
    dirs = os.listdir(Reportpath)
    dirs.sort()
    newreportname = dirs[-1]
    l.info('The new report name: {0}'.format(newreportname))
    # 创建一个带附件的邮件实例
    message=MIMEMultipart()
    # 邮件的其他属性
    message['From'] = send_name   #发送人
    message['Subject'] = Header(subject, 'utf8').encode()
    message['To'] = receive   #接收人
    # 邮件正文内容
    attr2 = MIMEText(text, 'plain', 'utf-8')
    message.attach(attr2)
    #构造附件
    path=os.path.join(Reportpath,newreportname)
    attr1=MIMEText(open(path,'rb').read(),'base64','utf-8')
    attr1["content_Type"]='application/octet-stream'
    attr1["Content-Disposition"] = 'attachment; filename="subject.html"'
    message.attach(attr1)
    try:
        server = smtplib.SMTP('smtp.163.com', 25)
        server.login(send_name, send_pwd)
        server.sendmail(send_name, receive,message.as_string())
        l.info("发送邮件至 {}".format(receive))
        l.info("发送邮件成功")
    except Exception as e:
        l.error('失败：' + str(e))


if __name__ == '__main__':
    sendmail()