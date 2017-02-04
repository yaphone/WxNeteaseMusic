#coding=utf-8
import subprocess
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#subprocess.Popen(['ping', 'www.baidu.com'])
info = subprocess.Popen('ping www.baidu.com', stdout=subprocess.PIPE)
print info.stdout.read().decode('gbk')