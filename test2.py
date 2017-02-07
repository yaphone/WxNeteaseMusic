#coding=utf-8
from subprocess import Popen, PIPE
from threading import Thread
import time


mp3_url = "http://m2.music.126.net/KpnMOcoD4bVewCspvWwi8g==/5845003813385723.mp3"
q = Popen("pkill mpg123", shell=True)
def test():
    p = Popen("mpg123 http://m2.music.126.net/KpnMOcoD4bVewCspvWwi8g==/5845003813385723.mp3", shell=True, stdout=PIPE)


def sing(mp3_url):
    try:
        console_info = Popen('mpg123 ' + mp3_url, shell=True, stdout=PIPE)
        time.sleep(3)
        #print console_info.stdout.read()
        #console_info = Popen('pkill mpg123', shell=True, stdout=PIPE)
        #print non_block_read(console_info.stdout)
    except:
        pass
    finally:
        #如果console_info信息包含“fail”字样，说明播放失败，自动播放下一曲
        console_info = Popen('mpg123 ' + mp3_url, shell=True, stdout=PIPE)
        #time.sleep(3)
        #print console_info.stdout.read()

def play():
    sing(mp3_url)

#play()
t = Thread(target=play)
t.start()