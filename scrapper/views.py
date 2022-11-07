from scrapper.domains import Melon
from scrapper.services import BugsMusic


class ScrapController(object):

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)


    @staticmethod
    def menu_2(arg):
        melon = Melon(arg)
        melon.scrap()
