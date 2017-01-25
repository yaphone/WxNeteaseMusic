#coding=utf-8

import itchat
import threading
import time

con = threading.Condition()
global playlist
playlist = []
music_list = [{'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u7ea2\u6708\u4eae2', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u7ea2\u6708\u4eae\u5973\u5b50\u5408\u5531\u56e2', 'mp3_url': u'http://m2.music.126.net/KpnMOcoD4bVewCspvWwi8g==/5845003813385723.mp3', 'playTime': '307592', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u5c71\u4e39\u4e39\u5f00\u82b1\u7ea2\u8273\u8273', 'quality': u'LD 96k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u539f\u58f0\u5730\u5e26', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u77f3\u6d77\u82f1', 'mp3_url': u'http://m2.music.126.net/8H2mAxd_1Astlow9S4J16A==/5681176580738588.mp3', 'playTime': '275879', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u7f9e\u7b54\u7b54\u7684\u73ab\u7470\u9759\u6084\u6084\u7684\u5f00', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u751c\u871c\u871c', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u9093\u4e3d\u541b', 'mp3_url': u'http://m2.music.126.net/MSmegzREx92Lh3ILSSz-gg==/1089616023133608.mp3', 'playTime': '211722', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u751c\u871c\u871c', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u5fd8\u60c5\u6c34', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u5218\u5fb7\u534e', 'mp3_url': u'http://m2.music.126.net/_trep5Lvydw2TjpEzJ8xDQ==/1163283302196025.mp3', 'playTime': '265456', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u5fd8\u60c5\u6c34', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u611f\u52a8', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u97e9\u7ea2', 'mp3_url': u'http://m2.music.126.net/W5D1GxLOpJIw5i6ssc8Lfw==/1009351674307029.mp3', 'playTime': '264673', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u5929\u8def', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u7231\u4e00\u4e2a\u4eba\u597d\u96be', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u82cf\u6c38\u5eb7', 'mp3_url': u'http://m2.music.126.net/7g0XjCa_vjF_NF-omgNXyQ==/1034640441745166.mp3', 'playTime': '245342', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u6211\u4e3a\u4f60\u4f24\u5fc3', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u4e60\u60ef\u4e86\u5bc2\u5bde', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u725b\u5976\u5496\u5561', 'mp3_url': u'http://m2.music.126.net/kcNpA8C-DeybJF8HE-Uitw==/1205064744050711.mp3', 'playTime': '305789', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u4e60\u60ef\u4e86\u5bc2\u5bde', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u79cb\uff1a\u6545\u4e8b', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u82cf\u6253\u7eff', 'mp3_url': u'http://m2.music.126.net/-aZIMxHu3zmntbe43Cn99w==/5510752278527338.mp3', 'playTime': '324288', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u6211\u597d\u60f3\u4f60', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u539f\u6765\u7231\u5c31\u662f\u751c\u871c \u7535\u89c6\u539f\u58f0\u5e26', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u90ed\u9759', 'mp3_url': u'http://m2.music.126.net/S0hnK4ga0RTarBKArZ1pVg==/1364493950637906.mp3', 'playTime': '239986', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u62e5\u62b1\u4f60\u7684\u5fae\u7b11', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u6076\u4f5c\u52672\u543b', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u8c22\u548c\u5f26', 'mp3_url': u'http://m2.music.126.net/k5b19enxgUTjtqzbjBe9yA==/6049512976074935.mp3', 'playTime': '222145', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u4f60\u66fe\u7ecf\u8ba9\u6211\u5fc3\u52a8', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u5c4b\u9876\u4e0a\u7684\u7eff\u5b9d\u77f3 \u7535\u89c6\u539f\u58f0\u5e26', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u5f20\u97f6\u6db5', 'mp3_url': u'http://m2.music.126.net/mvPV0m6y9N_D5c7UXd0Cnw==/1174278418472458.mp3', 'playTime': '244219', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u5176\u5b9e\u5f88\u7231\u4f60', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u6076\u4f5c\u5267\u4e4b\u543b \u7535\u89c6\u539f\u58f0\u5e26', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u738b\u4fde\u5300', 'mp3_url': u'http://m2.music.126.net/oKzMq-mLndgBDUD6pJoYRA==/2048390162555593.mp3', 'playTime': '208000', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u5168\u4e16\u754c\u7684\u4eba\u90fd\u77e5\u9053', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u542c\u7231', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u8c2d\u8273', 'mp3_url': u'http://m2.music.126.net/1zyg2KJxd5sTlJJfyKq-bQ==/5921969627449383.mp3', 'playTime': '311013', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u6700\u540e\u4e00\u591c', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u6211\u5f88\u5fd9', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u5468\u6770\u4f26', 'mp3_url': u'http://m2.music.126.net/VjCF_zOpaACkloQzvkMcTA==/7967061256324127.mp3', 'playTime': '288000', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u6211\u4e0d\u914d', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'\u6211\u4f9d\u7136\u7231\u4f60', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u8bb8\u8339\u82b8', 'mp3_url': u'http://m2.music.126.net/KltOZV9Q7yRVoeeq9T1j3Q==/1068725302206941.mp3', 'playTime': '252291', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u4e0d\u7231\u6211\u653e\u4e86\u6211', 'quality': u'HD 320k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'2014\u5e74\u592e\u89c6\u6625\u665a', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u738b\u94ee\u4eae', 'mp3_url': u'http://m2.music.126.net/BRRWn3jbW51W6HLhdeyMgw==/6024224208608487.mp3', 'playTime': '175056', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u65f6\u95f4\u90fd\u53bb\u54ea\u513f\u4e86', 'quality': u'MD 128k'}, {'\xe4\xb8\x93\xe8\xbe\x91\xef\xbc\x9a': u'2014\u5e74\u592e\u89c6\u6625\u665a', '\xe6\xad\x8c\xe6\x89\x8b\xef\xbc\x9a': u'\u9ec4\u6e24', 'mp3_url': u'http://m2.music.126.net/QvzaCl6ExZhvApxxjEXRCw==/5912074022695091.mp3', 'playTime': '186984', '\xe6\xad\x8c\xe6\x9b\xb2\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x9a': u'\u6211\u7684\u8981\u6c42\u4e0d\u7b97\u9ad8', 'quality': u'MD 128k'}]
music_list_1 = music_list[0:2]
music_list_2 = music_list[2:4]
music_list_3 = music_list[4:6]
music = [music_list_1, music_list_2, music_list_3]

def begin():
    itchat.auto_login()
    itchat.run()

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    #print(msg['Text'])
    text = msg['Text']
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

