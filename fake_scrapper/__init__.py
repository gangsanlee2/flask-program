from fake_scrapper.views import ScrappController
from util.common import Common

if __name__ == '__main__':
    api = ScrappController()
    while True:
        menus = ["종료", "벅스 뮤직"]
        menu = Common.menu(menus)
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            api.menu_1(menus[1])
        else:
            print(" ### 해당 메뉴 없음 ### ")