import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Bugs:         #class BugsMusic(object) 파이썬에서 object 생략 가능
    def __init__(self,url):
        self.url = url

    def scrap(self):
        req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req), 'lxml')
        _ = 0
        title = {"class": "title"}
        artist = {"class": "artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        for i, j in zip(titles, artists):
            _ += 1
            print(f"{_}위 {i.find('a').text} - {j.find('a').text}")

class Melon:
    def __init__(self,url):
        self.url = url

    def scrap(self):
        req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req), 'lxml')
        title = {"class": "ellipsis rank01"}
        artist = {"class": "ellipsis rank02"}
        titles = soup.find_all(name="div", attrs=title)
        artists = soup.find_all(name="div", attrs=artist)
        [print(f"{i + 1}위 {j.find('a').text} : {k.find('a').text}")
         for i, j, k in zip(range(len(titles)), titles, artists)]