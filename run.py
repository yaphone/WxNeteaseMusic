#coding=utf-8
import itchat
import threading
import time
import subprocess
from myapi import MyNetease
from menu import help_msg
import os

con = threading.Condition()

global playlist, music_list, help_msg, userId, myNetease
myNetease = MyNetease()
playlist = myNetease.get_music_list()
#playlist = []

def begin():
    itchat.auto_login()
    itchat.run(debug=True)

@itchat.msg_register(itchat.content.TEXT)
def mp3_player(msg):
    text = msg['Text']
    res = msg_handler(text)
    return res

def msg_handler(args):
    global myNetease
    arg_list = args.split(" ")    #参数以空格为分割符
    if len(arg_list) == 1:  #如果接收长度为1
        msg = arg_list[0]
        res = ""
        if msg == u'H': #帮助信息
            res = help_msg
        elif msg == u'N': #下一曲
            if con.acquire():
                con.notifyAll()
                con.release()
            res = u'切换成功，正在播放: ' + playlist[0].get('song_name')
        elif msg == u'P': #上一曲
            if len(playlist) < 2:
                res = u'当前播放列表只有一首歌曲'
            else:#取出列表中的最后两首歌，放在列表头部
                s_tmp_playlist = playlist[:-2]
                e_tmp_playlist = playlist[-2:]
                global playlist
                playlist = e_tmp_playlist + s_tmp_playlist
                res = u'切换成功，正在播放: ' + playlist[0].get('song_name')
            if con.acquire():
                con.notifyAll()
                con.release()
        elif msg == u'U':  #用户歌单
            user_playlist = myNetease.get_user_playlist()
            if user_playlist == -1:
                res = u"用户播放列表为空"
            else:
                index = 0
                for data in user_playlist:
                    res += str(index) + ". " + data['name'] + "\n"
                    index += 1
                res += u"\n 输入 U 序号 切换歌单"

        elif msg == u'M': #当前歌单播放列表
            res = ""
            global  playlist
            if len(playlist) == 0:
                res = u"当前播放列表为空，请回复 (U) 选择播放列表"
            i = 0
            for song in playlist:
                res += str(i) + ". " + song["song_name"] + "\n"
                i += 1
        elif msg == u'R': #当前正在播放的歌曲信息
            song_info = playlist[-1]
            artist = song_info.get("artist")
            song_name = song_info.get("song_name")
            album_name = song_info.get("album_name")
            res = u"歌曲：" + song_name + u"\n歌手：" + artist + u"\n专辑：" + album_name
        elif msg == u"S": #单曲搜索
            res = u"回复 (S 歌曲名) 进行搜索"

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
    elif len(arg_list) == 2:  #接收信息长度为2
        arg1 = arg_list[0]
        arg2 = arg_list[1]
        if arg1 == u"U":
            user_playlist = myNetease.get_user_playlist()
            if user_playlist == -1:
                res = u"用户播放列表为空"
            else:
                try:
                    index = int(arg2)
                    data = user_playlist[index]
                    playlist_id = data['id']   #歌单序号
                    song_list = myNetease.get_song_list_by_playlist_id(playlist_id)
                    playlist = song_list
                    res = u"播放列表切换成功，回复M可查看当前播放列表"
                    if con.acquire():
                        con.notifyAll()
                        con.release()
                except:
                    res = u"输入有误"
        elif arg1 == u'N': #播放第X首歌曲
            index = int(arg2)
            tmp_song = playlist[index]
            playlist.insert(0, tmp_song)
            if con.acquire():
                con.notifyAll()
                con.release()
            res = u'切换成功，正在播放: ' + playlist[0].get('song_name')
            del playlist[-1]
        elif arg1 == u"S": #歌曲搜索+歌曲名
            song_name = arg2
            song_list = myNetease.search_by_name(song_name)
            res = ""
            i = 0
            for song in song_list:
                res += str(i) + ". " + song["song_name"] + "\n"
                i += 1
            res += u"回复（S 歌曲名 序号）播放对应歌曲"

    elif len(arg_list) == 3:   #接收长度为3
        arg1 = arg_list[0]
        arg2 = arg_list[1]
        arg3 = arg_list[2]
        try:
            if arg1 == u'L':  #用户登陆
                res = myNetease.login(arg2, arg3)
            elif arg1 == u"S":
                song_name = arg2
                song_list = myNetease.search_by_name(song_name)
                index = int(arg3)
                song = song_list[index]
                #把song放在播放列表的第一位置，唤醒播放线程，立即播放
                playlist.insert(0, song)
                if con.acquire():
                    con.notifyAll()
                    con.release()
                artist = song.get("artist")
                song_name = song.get("song_name")
                album_name = song.get("album_name")
                res = u"歌曲：" + song_name + u"\n歌手：" + artist + u"\n专辑：" + album_name
        except:
            res = u"输入错误"

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
                mp3_url = song["mp3_url"]
                sing(mp3_url)
                con.notifyAll()
                con.wait(int(song.get('playTime'))/1000)


#播放MP3文件
def sing(mp3_url):
    try:
        subprocess.Popen('pkill mpg123', shell=True, stdout=subprocess.PIPE)
    except:
        pass
    finally:
        subprocess.Popen('mpg123 ' + mp3_url, shell=True, stdout=subprocess.PIPE)



if __name__ == '__main__':
    t1 = threading.Thread(target=begin)
    t2 = threading.Thread(target=play)
    t1.start()
    t2.start()

