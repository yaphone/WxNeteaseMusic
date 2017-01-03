#!/usr/bin/env python
#encoding: UTF-8

from  neteaseApi import api
import hashlib

def main():
    netease = api.NetEase()
    username = 'zhouyaphone@163.com'
    password = 'WO19891226'
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    #login_info = netease.login(username, password)
    #print login_info
    #print str(login_info.get('message')) + " " + login_info.get('captchaId')
    #userId = login_info.get('profile').get('userId') #用户歌单
    userId = 57542828
    playlist = netease.user_playlist(userId) #用户歌单
    print playlist
    if playlist == -1:
        return
    datatype = 'top_playlists'
    datalist = netease.dig_info(playlist, datatype)
    title =  username + ' 的歌单'
    #print title
    #for data in datalist:
    #    print str(data.get('playlist_id')) + " " + data.get('creator_name') + " " + data.get('playlists_name')
    #songs = netease.playlist_detail(556989108)  #歌单详情
    songs = netease.playlist_detail(57542828)  # 歌单详情
    datalist = netease.dig_info(songs, 'songs')
    music_list = []
    for data in datalist:
        music_info = {}
        music_info.setdefault("歌曲名称：", data.get("song_name"))
        music_info.setdefault("歌手：", data.get("artist"))
        music_info.setdefault("专辑：", data.get("album_name"))
        music_info.setdefault("mp3_url", data.get("mp3_url"))
        music_info.setdefault("playTime", data.get("playTime"))  #音乐时长
        music_list.append(music_info)
        music_info.setdefault("quality", data.get("quality"))
'''
    for music in music_list:
        for key, value in music.items():
            print key, value
'''
 #   print songs


if __name__ == '__main__':
    main()