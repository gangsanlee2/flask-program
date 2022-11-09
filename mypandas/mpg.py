# oop로 바꿔보기

import pandas as pd

mpg = pd.read_csv('./data/mpg.csv')

def menu_1():
    print(mpg.head())

def menu_2():
    print(mpg.tail())

def menu_3():
    print(mpg.shape)

def menu_4():
    print(mpg.info())

def menu_5():
    print(mpg.describe())

def menu_6():
    print(mpg.describe(include='all'))

if __name__ == "__main__":
    while True:
        menu = ["종료", "mpg 앞부분 확인", "mpg 뒷부분 확인", "행, 열 출력", "데이터 속성 확인", "요약 통계량 출력", "문자 변수 요약 통계량 함께 출력"]
        for i, j in enumerate(menu):
            print(f'{i}.{j}')
        choice = int(input('메뉴 입력 : '))
        if choice == 0:
            print(menu[0])
            break
        elif choice == 1:
            print(menu[1])
            menu_1()
        elif choice == 2:
            print(menu[2])
            menu_2()
        elif choice == 3:
            print(menu[3])
            menu_3()
        elif choice == 4:
            print(menu[4])
            menu_4()
        elif choice == 5:
            print(menu[5])
            menu_5()
        elif choice == 6:
            print(menu[6])
            menu_6()
        else:
            print(" 잘못된 메뉴 입력 ")