#coding=utf-8

import itchat
import threading
from api import get_music_list
from menu import help_msg

con = threading.Condition()

global playlist, music_list, help_msg
playlist = get_music_list()
music_list = get_music_list()
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

def msg_handler(msg):
    res = ""
    if msg == u'H': #帮助信息
        res = help_msg
    elif msg == u'N': #下一曲
        pass
    elif msg == u'P': #上一曲
        pass
    elif msg == u'M': #播放列表
        res = ""
        i = 0
        for song in playlist:
            res += str(i) + ". " + song["song_name"] + "\n"
            i += 1
        print res
    else:
        try:
            index = int(msg)
            if index > len(playlist) - 1:
                res = u"输入不正确"
            else:
                if con.acquire():
                    song = playlist[index]
                    playlist.remove(song)
                    playlist.append(song)
                    #for key, val in song.items():
                    #    print key, val
                    con.notifyAll()
                    # self.con.wait(int(song.get('playTime'))/100000)
                    con.wait(10)

        except:
            res = u'错误'

    return res

def play():
    while True:
        if con.acquire():
            global playlist
            if playlist:
                # 循环播放，取出第一首歌曲，放在最后的位置，类似一个循环队列
                # print playlist
                song = playlist[0]
                playlist.remove(song)
                playlist.append(song)
                for key, val in song.items():
                    print key, val
                con.notifyAll()
                # self.con.wait(int(song.get('playTime'))/100000)
                con.wait(10)




if __name__ == '__main__':
    t1 = threading.Thread(target=begin)
    t2 = threading.Thread(target=play)
    t1.start()
    #t2.start()

