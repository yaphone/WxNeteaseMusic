#coding=utf-8
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3

def get_mp3_info(mp3_url):
    id3info = MP3(mp3_url, ID3=EasyID3)
    for k, v in id3info.items():
        print k, v




if __name__ == '__main__':
    mp3_url = 'http://m1.music.126.net/gdmi6WMy6as24I8JNeLmPg==/18632324045084368.mp3'
    get_mp3_info(mp3_url)