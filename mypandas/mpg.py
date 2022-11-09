import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MENU = ["종료",
        "mpg 앞부분 확인",
        "mpg 뒷부분 확인",
        "행, 열 출력",
        "데이터 속성 확인",
        "요약 통계량 출력",
        "문자 변수 요약 통계량 함께 출력",
        "manufacturer를 company로 변경",
        "test 변수 생성",
        # cty 와 hwy 변수를 머지(merge)하여 total
        # 변수 생성하고 20이상이면 pass 미만이면 fail 저장
        "test 빈도표 만들기",
        "test 빈도 막대 그래프 그리기",
        # mpg 144페이지 문제
        "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
        "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
        "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
        # mpg 150페이지 문제
        # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
        # 후 다음 문제 풀이
        "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?",
        # mpg 153페이지 문제
        "아우디차에서 고속도로 연비 1~5위 출력하시오",
        # mpg 158페이지 문제
        "평균연비가 가장 높은 자동차 1~3위 출력하시오"]

class Mpg:
    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')
    def menu_1(self):
        print(self.mpg.head())

    def menu_2(self):
        print(self.mpg.tail())

    def menu_3(self):
        print(self.mpg.shape)

    def menu_4(self):
        print(self.mpg.info())

    def menu_5(self):
        print(self.mpg.describe())

    def menu_6(self):
        print(self.mpg.describe(include='all'))

    def menu_7(self):
        print(self.mpg.rename(columns={'manufacturer':'company'}))

    def menu_8(self):
        mpg = self.mpg
        mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
        mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
        print(mpg)

    def menu_9(self):
        self.menu_8()
        self.count_test = self.mpg['test'].value_counts()
        print(self.count_test)

    def menu_10(self):
        self.menu_9()
        self.count_test.plot.bar(rot=0)
        plt.savefig('./save/mpg_graph.jpg')

    def menu_11(self):
        avg_s = self.mpg.query('displ <= 4')['hwy'].mean()
        avg_b = self.mpg.query('displ >= 5')['hwy'].mean()
        if avg_s > avg_b:
            print('배기량이 4 이하인 자동차가 5 이상인 자동차보다 고속도로 연비 평균이 더 높다')
        elif avg_s == avg_b:
            print('배기량이 4 이하인 자동차와 5 이상인 자동차의 고속도로 연비 평균이 같다')
        else:
            print('배기량이 4 이하인 자동차가 5 이상인 자동차보다 고속도로 연비 평균이 더 낮다')

    def menu_12(self):
        avg_a = self.mpg.query('manufacturer == "audi"')['cty'].mean()
        avg_t = self.mpg.query('manufacturer == "toyota"')['cty'].mean()
        if avg_a > avg_t:
            print('아우디가 토요타보다 도시 연비가 평균적으로 더 높다')
        elif avg_a == avg_t:
            print('아우디와 토요타의 평균 도시 연비는 같다')
        else:
            print('아우디가 토요타보다 도시 연비가 평균적으로 더 낮다')

    def menu_13(self):
        cfh = self.mpg.query('manufacturer == "chevrolet" | manufacturer == "ford" | manufacturer == "honda"')
        print(cfh['hwy'].mean())

    def menu_14(self):
        mpg = self.mpg.rename(columns={'class':'category'})
        mpg = mpg[['category','cty']]
        avg_s = mpg.query('category == "suv"')['cty'].mean()
        avg_c = mpg.query('category == "compact"')['cty'].mean()
        if avg_s > avg_c:
            print('suv가 compact보다 평균적으로 도시 연비가 더 높다')
        elif avg_s == avg_c:
            print('suv와 compact의 평균 도시 연비는 같다')
        else: print('suv가 compact보다 평균적으로 도시 연비가 더 낮다')

    def menu_15(self):
        mpg = self.mpg.query('manufacturer == "audi"')
        mpg = mpg.sort_values('cty', ascending=False)
        mpg = mpg[['manufacturer','model','cty']]
        print(mpg.head())

    def menu_16(self):
        mpg = self.mpg
        mpg['avg_mpg'] = (mpg['cty'] + mpg['hwy'])/2
        mpg = mpg.sort_values('avg_mpg', ascending=False)
        print(mpg.head(n=3))


if __name__ == "__main__":
    m = Mpg()
    while True:
        menu = MENU        
        for i, j in enumerate(menu):
            print(f'{i}.{j}')
        choice = int(input('메뉴 입력 : '))
        if choice == 0:
            print(menu[0])
            break
        elif choice == 1:
            print(menu[1])
            m.menu_1()
            print("*" * 100)
        elif choice == 2:
            print(menu[2])
            m.menu_2()
            print("*" * 100)
        elif choice == 3:
            print(menu[3])
            m.menu_3()
            print("*" * 100)
        elif choice == 4:
            print(menu[4])
            m.menu_4()
            print("*" * 100)
        elif choice == 5:
            print(menu[5])
            m.menu_5()
            print("*" * 100)
        elif choice == 6:
            print(menu[6])
            m.menu_6()
            print("*" * 100)
        elif choice == 7:
            print(menu[7])
            m.menu_7()
            print("*" * 100)
        elif choice == 8:
            print(menu[8])
            m.menu_8()
            print("*" * 100)
        elif choice == 9:
            print(menu[9])
            m.menu_9()
            print("*" * 100)
        elif choice == 10:
            print(menu[10])
            m.menu_10()
            print("*" * 100)
        elif choice == 11:
            print(menu[11])
            m.menu_11()
            print("*" * 100)
        elif choice == 12:
            print(menu[12])
            m.menu_12()
            print("*" * 100)
        elif choice == 13:
            print(menu[13])
            m.menu_13()
            print("*" * 100)
        elif choice == 14:
            print(menu[14])
            m.menu_14()
            print("*" * 100)
        elif choice == 15:
            print(menu[15])
            m.menu_15()
            print("*" * 100)
        elif choice == 16:
            print(menu[16])
            m.menu_16()
            print("*" * 100)
        else:
            print(" 잘못된 메뉴 입력 ")