from scrapper.domains import Scrap
from scrapper.views import ScrapController
from util.common import Common

if __name__ == '__main__':
    api = ScrapController()
    scrap = Scrap()
    while True:
        menus = ["종료","벅스 뮤직","멜론"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names=["title","artist"]
            scrap.tag_name = "p"
            scrap.path = './save/result.csv'
            api.menu_1(scrap)
        elif menu == "2":
            print(menus[2])
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime=2022110817"
            scrap.query_string = "2022110817"
            scrap.parser = "lxml"
            scrap.class_names = ["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            scrap.path = './save/result.csv'
            api.menu_2(scrap)
        else:
            print(" ### 해당 메뉴 없음 ### ")