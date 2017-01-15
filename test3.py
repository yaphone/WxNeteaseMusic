global a
a = 3

class Test():
    def fun(self):
        global a
        for i in range(10):
            a += 1
            print a

t = Test()
t.fun()