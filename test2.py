#coding=utf-8
import threading
import time

con = threading.Condition()

class Test1(threading.Thread):
    def __init__(self):
        super(Test1, self).__init__()
        self.con = con
    def run(self):
        self.con.acquire()
        while True:
            print "Hello"
            con.notifyAll()
            con.wait()

class Test2(threading.Thread):
    def __init__(self):
        super(Test2, self).__init__()
        self.con = con
    def run(self):
        self.con.acquire()
        while True:
            print "请输入："
            s = raw_input()
            print "输入：" + s
            con.notifyAll()
            con.wait()

t1 = Test1()
t2 = Test2()
t2.start()
t1.start()

