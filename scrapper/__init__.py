from scrapper.views import ScrapController
from util.common import Common

if __name__ == '__main__':
    api = ScrapController()
    while True:
        menus = ["종료","벅스 뮤직"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            api.menu_1(arg="https://music.bugs.co.kr/chart/track/day/total")
        else:
            print(" ### 해당 메뉴 없음 ### ")