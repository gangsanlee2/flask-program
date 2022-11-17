'''
위도 latitude 0~90grade NS
경도 longtitude 0~180grade WS
'''

import googlemaps
import numpy as np
import pandas as pd

CRIME_MENUS = ["close", # 0
               "spec", # 1
               "Merge", # 2
               "interval", # 3
               "ratio", # 4
               "nominal", # 5
               "ordinal", # 6
               "tatget", # 7
               "partition" # 8
               ]

crime_menu = {"1": lambda t: t.spec(),
              "2": lambda t: t.save_police_pos(),
              "3": lambda t: t.interval(),
              "4": lambda t: t.ratio(),
              "5": lambda t: t.nominal(),
              "6": lambda t: t.ordinal(),
              "7": lambda t: t.target(),
              "8": lambda t: t.partition()
              }

class CrimeService:
    def __init__(self):
        self.crime = pd.read_csv("./data/crime_in_seoul.csv")
        self.cctv = pd.read_csv("./data/cctv_in_seoul.csv")
        self.ls = [self.crime,self.cctv]
        self.pop = pd.read_excel(io="./data/pop_in_seoul.xls", header=1,
                                 usecols=['자치구','합계','한국인','등록외국인','65세이상고령자'], skiprows=[2])

    '''
    def temp(self):
        def sub(x):
            print(" --- 1.Shape ---")
            print(x.shape)
            print(" --- 2.Features ---")
            print(x.columns)
            print(" --- 3.Info ---")
            print(x.info())
            print(" --- 4.Case Top1 ---")
            print(x.head(1))
            print(" --- 5.Case Bottom1 ---")
            print(x.tail(3))
            print(" --- 6.Describe ---")
            print(x.describe())
            print(" --- 7.Describe All ---")
            print(x.describe(include='all'))
        return sub
        
    def spec(self):
        s = self.temp()
        s(self.crime)
        s(self.cctv)
    '''

    def spec(self):
        [(lambda x: print(f" --- 1.Shape ---\n"
                          f"{x.shape}\n"
                          f" --- 2.Features --- \n"
                          f"{x.columns}\n"
                          f" --- 3.Info ---\n"
                          f"{x.info()}\n"
                          f" --- 4.Case Top1 ---\n"
                          f"{x.head(1)}\n"
                          f" --- 5.Case Bottom1 ---\n"
                          f"{x.tail(3)}\n"
                          f" --- 6.Describe ---\n"
                          f"{x.describe()}\n"
                          f" --- 7.Describe All ---\n"
                          f"{x.describe(include='all')}"))(i)
         for i in self.ls]

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f'지역이름: {name}')
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f' 서울시내 경찰서는 총 {len(station_names)}개 이다')
        [print(f'{str(i)}') for i in station_names]
        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print(' ### API에서 주소추출 시작 ### ')
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] =='구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv', index=False)
        crime.to_pickle('./save/police_pos.pkl')
        df = pd.read_pickle('./save/police_pos.pkl')
        print(df)

    def save_cctv_pos(self):
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]:'구별'}, inplace=True)
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
        }, inplace=True)
        pop.drop(index=26,inplace=True)
        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        cctv.drop(['2013년도 이전','2014년','2015년','2016년'], axis=1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구별")
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        cctv_pop.to_pickle("./save/cctv_pop.pkl")
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """

    def interval(self):
        pass

    def ratio(self):
        pass

    def nominal(self):
        pass

    def ordinal(self):
        pass

    def target(self):
        pass

    def partition(self):
        pass

if __name__ == '__main__':
    c = CrimeService()
    c.save_cctv_pos()