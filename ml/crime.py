import googlemaps
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
        self.pop = pd.read_excel("./data/pop_in_seoul.xls", header=1,
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
    print(c.pop.head())