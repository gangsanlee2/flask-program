import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Midwest:
    def __init__(self):
        self.midwest = pd.read_csv('./data/midwest.csv')

    def menu_1(self):
        print(self.midwest)
        print(self.midwest.info())

    def menu_2(self):
        self.midwest = self.midwest.rename(columns={'poptotal':'total','popasian':'asian'})
        print(self.midwest.info())

    def menu_3(self):
        self.midwest = self.midwest.rename(columns={'poptotal': 'total', 'popasian': 'asian'})
        self.midwest['rate_asian'] = (self.midwest['asian'] / self.midwest['total']) * 100
        print(self.midwest)

    def menu_4(self):
        self.midwest = self.midwest.rename(columns={'poptotal': 'total', 'popasian': 'asian'})
        self.midwest['rate_asian'] = (self.midwest['asian'] / self.midwest['total']) * 100
        avg_rate_asian = sum(self.midwest['rate_asian'])/len(self.midwest['rate_asian'])
        self.midwest['size_popasian'] = np.where(self.midwest['rate_asian']>avg_rate_asian,'large','small')
        print(self.midwest)

    def menu_5(self):
        self.midwest = self.midwest.rename(columns={'poptotal': 'total', 'popasian': 'asian'})
        self.midwest['rate_asian'] = (self.midwest['asian'] / self.midwest['total']) * 100
        avg_rate_asian = sum(self.midwest['rate_asian']) / len(self.midwest['rate_asian'])
        self.midwest['size_popasian'] = np.where(self.midwest['rate_asian'] > avg_rate_asian, 'large', 'small')
        count_test = self.midwest['size_popasian'].value_counts()
        count_test.plot.bar(rot = 0)
        plt.savefig('./save/midwest_graph.jpg')



if __name__ == "__main__":
    m = Midwest()
    while True:
        menu = ["종료","메타데이터 출력","poptotal/popasian 변수를 total/asian로 이름변경",
                "전체 인구 대비 아시아 인구 백분율 변수 추가","아시아 인구 백분율 전체 평균을 large/small 로 분류",
                "large/small 빈도표와 빈도막대그래프 작성"]
        for i, j in enumerate(menu):
            print(f'{i}.{j}')
        choice = int(input('메뉴 입력 : '))
        if choice == 0:
            print(menu[0])
            break
        elif choice == 1:
            print(menu[1])
            m.menu_1()
        elif choice == 2:
            print(menu[2])
            m.menu_2()
        elif choice == 3:
            print(menu[3])
            m.menu_3()
        elif choice == 4:
            print(menu[4])
            m.menu_4()
        elif choice == 5:
            print(menu[5])
            m.menu_5()
        else:
            print(" 잘못된 메뉴 입력 ")