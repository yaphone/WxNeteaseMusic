#coding=utf-8
from subprocess import PIPE, Popen
import sys
from threading import Thread
from Queue import Queue

def enqueue_output(out, queue):
    for line in iter(out.readline, b""):
        queue.put(line)
    out.close()
ON_POSIX = "posix" in sys.builtin_module_names

p = Popen("ls -l", shell=True, stdout=PIPE, close_fds=ON_POSIX)
q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True
t.start()

try:
    line = q.get_nowait()
except:
    print "***********"
else:
    print line
