import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup

from fake_scrapper.domains import Bugs, Melon


class ScrapController:

    @staticmethod
    def menu_1(url):
        bugs = Bugs(url)
        bugs.scrap()


    @staticmethod
    def menu_2(url):
        melon = Melon(url)
        melon.scrap()