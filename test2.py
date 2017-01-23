#coding:utf-8
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
            con.wait(3)

class Test2(threading.Thread):
    def __init__(self):
        super(Test2, self).__init__()
        self.con = con
    def run(self):
        self.con.acquire()
        while True:
            print "Please input:"
            #s = raw_input()
            #print "input:" + s
            #con.notifyAll()
            #con.wait()
            time.sleep(1)

t1 = Test1()
t2 = Test2()
t1.start()
t2.start()


