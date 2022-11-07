from fake_scrapper.views import ScrapController

if __name__ == "__main__":
    while True:
        api = ScrapController()
        ls = ["close", "bugs", "melon"]
        for i,j in enumerate(ls):
            print(f"{i}.{j}")
        menu = int(input("메뉴선택 : "))
        if menu == 0:
            print(ls[0])
            break
        elif menu == 1:
            print(ls[1])
            api.menu_1(url="https://music.bugs.co.kr/chart/track/realtime/total")
        elif menu == 2:
            print(ls[2])
            api.menu_2(url="https://www.melon.com/chart/index.htm")
        else:
            print(" wrong menu ")




