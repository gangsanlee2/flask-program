import urllib
from dataclasses import dataclass
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

@dataclass
class Scrap:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None
    soup = BeautifulSoup


    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = 'save/fake_melon_rank.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)

def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i+1}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(0, len(titles)), titles, artists)]
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장


def MelonMusic(arg):
    req = urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i+1}위 {j} : {k}")  # 디버깅
     for i, j, k in zip(range(0, len(titles)), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()  # csv파일로 저장


class ScrapController:
    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)
    @staticmethod
    def menu_2(arg):
        MelonMusic(arg)


if __name__=="__main__":
    scrap = Scrap()
    api = ScrapController()
    while True:
        menu = input("0번:종료,1번:벅스,2번:멜론")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names=["title", "artist"]
            scrap.tag_name = "p"
            api.menu_1(scrap)
        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110808"
            scrap.parser = "lxml"
            scrap.class_names=["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            api.menu_2(scrap)
        else:
            print("해당메뉴 없음")