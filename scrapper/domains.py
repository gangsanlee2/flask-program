# db에 저장할거면 모델(도메인) 쓰고 더이상 필요없으면 services에서 함수형으로 사용
from dataclasses import dataclass
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""
"""
class BugsMusic:    #class BugsMusic(object) 파이썬에서 object 생략 가능
        
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url),'lxml')
        # print(soup.prettify(encoding="UTF8")) 무작정 추출하면 안됨! -> 원하는 정보만 스크랩하는게 중요!
        _ = 0
        title = {"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        
        '''
        for i in titles: #여기서 titles는 시퀀스 자료구조
            print(f"{i.find('a').text}")
        print("*"*20)
        for i in artists:
            print(f"{i.find('a').text}")
        print("*"*20)
        '''
        
        for i,j in zip(titles,artists):
            _ += 1
            print(f"{_}위 {i.find('a').text} - {j.find('a').text}")
        
class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        soup = BeautifulSoup(urlopen(req),'lxml')
        _ = 0
        title = {"class":"ellipsis rank01"}
        artist = {"class":"ellipsis rank02"}
        titles = soup.find_all(name="div", attrs=title)
        artists = soup.find_all(name="div", attrs=artist)
        for i,j in zip(titles, artists):
            _ += 1
            print(f"{_}위 {i.find('a').text} - {j.find('a').text}")
"""
@dataclass
class MusicRanking:
    html : str
    parser : str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname : str
    class_names : list
    artists : list
    titles : list
    dic : dict
    df : None
    soup : BeautifulSoup

    @property
    def html(self): return self._html
    @html.setter
    def context(self, html): self._html = html
    @property
    def parser(self): return self._parser
    @parser.setter
    def context(self, parser): self._parser = parser
    @property
    def domain(self): return self._domain
    @domain.setter
    def context(self, domain): self._domain = domain
    @property
    def query_string(self): return self._query_string
    @query_string.setter
    def context(self, query_string): self._query_string = query_string
    @property
    def headers(self): return self._headers
    @headers.setter
    def context(self, headers): self._headers = headers
    @property
    def tag_name(self): return self._tag_name
    @tag_name.setter
    def context(self, tag_name): self._tag_name = tag_name
    @property
    def fname(self): return self._fname
    @fname.setter
    def context(self, fname): self._fname = fname
    @property
    def class_names(self): return self._class_names
    @class_names.setter
    def context(self, class_names): self._class_names = class_names
    @property
    def artists(self): return self._artists
    @artists.setter
    def context(self, artists): self._artists = artists
    @property
    def titles(self): return self._titles
    @titles.setter
    def context(self, titles): self._titles = titles
    @property
    def dic(self): return self._dic
    @dic.setter
    def context(self, dic): self._dic = dic
    @property
    def df(self): return self._df
    @df.setter
    def context(self, df): self._df = df
    @property
    def soup(self) -> BeautifulSoup: return self._soup
    @soup.setter
    def train(self, soup): self._soup = soup

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):
        path = CTX+self.fname+'.csv'
        self.df.to_csv(path, sep=',',na_rep="NaN")