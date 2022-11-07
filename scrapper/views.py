from scrapper.domains import BugsMusic


class ScrapController(object):

    @staticmethod
    def menu_1(arg):
        bugs = BugsMusic(arg)
        bugs.scrap()