#coding=utf-8
from subprocess import PIPE, Popen
import sys
from threading import Thread
from Queue import Queue
import mp3play
import time

#mp3 = mp3play.load("http://m2.music.126.net/KpnMOcoD4bVewCspvWwi8g==/5845003813385723.mp3")
#mp3.play()
#time.sleep(300)
L = [1, 2, 3]
del L[-1]
print L
