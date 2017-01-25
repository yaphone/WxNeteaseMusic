#coding=utf-8

import itchat
import threading
from api import get_music_list

con = threading.Condition()

global playlist, music_list, help_msg
playlist = []
music_list = get_music_list()
help_msg = u"1. H(elp): 帮助信息\n" \
           u"2. L(ogin): 登陆网易云音乐\n" \
           u"3. M(usicList): 音乐歌单\n" \
           u"4. P(revious): 上一曲\n" \
           u"5. N(ext): 下一曲\n"

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
    #print res
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
    if msg == u'H':
        return help_msg

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
    t2.start()

