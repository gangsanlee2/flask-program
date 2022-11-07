# db에 저장할거면 모델(도메인) 쓰고 더이상 필요없으면 services에서 함수형으로 사용
from urllib.request import urlopen

from bs4 import BeautifulSoup


class BugsMusic:    #class BugsMusic(object) 파이썬에서 object 생략 가능
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url),'lxml')
        print(soup.prettify(encoding="UTF8"))