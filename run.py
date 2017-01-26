#coding=utf-8

import itchat
import threading
import time
import subprocess
from myapi import get_music_list, login, get_user_playlist
from menu import help_msg

con = threading.Condition()

global playlist, music_list, help_msg, userId
playlist = get_music_list()
music_list = get_music_list()
userId = int(open("./userInfo", 'r').read())
music_list_1 = music_list[0:2]
music_list_2 = music_list[2:4]
music_list_3 = music_list[4:6]
music = [music_list_1, music_list_2, music_list_3]

def begin():
    itchat.auto_login()
    itchat.run(debug=False)

@itchat.msg_register(itchat.content.TEXT)
def mp3_player(msg):
    text = msg['Text']
    res = msg_handler(text)
    return res
    '''
    try:
        num = int(text)
        global playlist
        playlist = music[num]
        if con.acquire():
            con.notifyAll()
            con.release()
        #print playlist
    except:
        print "输入有误"
    '''

def msg_handler(args):
    arg_list = args.split(" ")    #以空格为分割符
    if len(arg_list) == 1:  #如果接收长度为1
        msg = arg_list[0]
        res = ""
        if msg == u'H': #帮助信息
            res = help_msg
        elif msg == u'N': #下一曲
            if con.acquire():
                con.notifyAll()
                con.release()
        elif msg == u'P': #上一曲
            pass
        elif msg == u'U':  #用户歌单
            user_playlist = get_user_playlist(userId)
            #print user_playlist
            if user_playlist == -1:
                res = u"用户列表为空"
            else:


        elif msg == u'M': #当前歌单播放列表
            res = ""
            i = 0
            for song in playlist:
                res += str(i) + ". " + song["song_name"] + "\n"
                i += 1
        else:
            try:
                index = int(msg)
                if index > len(playlist) - 1:
                    res = u"输入不正确"
                else:
                    if con.acquire():
                        con.notifyAll()
                        con.release()

            except:
                res = u'错误'
    if len(arg_list) == 2:  #接收信息长度为2
        pass

    if len(arg_list) == 3:   #接收长度为3
        arg1 = arg_list[0]
        arg2 = arg_list[1]
        arg3 = arg_list[2]
        if arg1 == u'L':
            res = login(arg2, arg3)

    return res

def play():
    while True:
        if con.acquire():
            global playlist
            if playlist:
                # 循环播放，取出第一首歌曲，放在最后的位置，类似一个循环队列
                song = playlist[0]
                playlist.remove(song)
                playlist.append(song)
                #for key, val in song.items():
                #    print key, val
                mp3_url = song["mp3_url"]
                sing(mp3_url)
                con.notifyAll()
                # self.con.wait(int(song.get('playTime'))/100000)
                con.wait(int(song.get('playTime'))/1000)
                #con.wait(10)

def sing(mp3_url):
    try:
        subprocess.Popen(['pkill', 'mpg123'])
        time.sleep(.3)
    except:
        pass
    finally:
        subprocess.Popen(['mpg123', mp3_url])



if __name__ == '__main__':
    t1 = threading.Thread(target=begin)
    t2 = threading.Thread(target=play)
    t1.start()
    t2.start()

