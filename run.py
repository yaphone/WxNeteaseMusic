#!/usr/bin/env python
#encoding: UTF-8

from  neteaseApi import api
import hashlib

def main():
    netease = api.NetEase()
    username = 'zhouyaphone@163.com'
    password = 'WO19891226'
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    login_info = netease.login(username, password)
    print login_info.get('message') + " " + login_info.get('captchaId')
    userId = login_info.get('profile').get('userId') #用户歌单
    playlist = netease.user_playlist(userId) #用户歌单
    if playlist == -1:
        return
    datatype = 'top_playlists'
    datalist = netease.dig_info(playlist, datatype)
    title =  username + ' 的歌单'
    print title
    print datalist
    for data in datalist:
        print str(data.get('playlist_id')) + " " + data.get('creator_name') + " " + data.get('playlists_name')


if __name__ == '__main__':
    main()