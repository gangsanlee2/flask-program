from scrapper.domains import MusicRanking
from scrapper.views import ScrapController
from util.common import Common

if __name__ == '__main__':
    api = ScrapController()
    m = MusicRanking()
    while True:
        menus = ["종료","벅스 뮤직","멜론"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221101"
            m.parser = "lxml"
            m.class_names.append("title")
            m.class_names.append("artist")
            m.tag_name = "p"
            api.menu_1(m)
        elif menu == "2":
            print(menus[2])
            api.menu_2(arg="https://www.melon.com/chart/index.htm")
        else:
            print(" ### 해당 메뉴 없음 ### ")