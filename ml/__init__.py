from ml.crime import CrimeService, CRIME_MENUS, crime_menu

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = CrimeService()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            crime_menu[menu](t)
            try:
                crime_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")