from bicycle.views import BicycleController
from util.common import Common

api = BicycleController()
while True:
    menu = Common.menu(["종료","시각화","모델링","머신러닝","배포"])
    if menu == "0": break
    elif menu == "1":
        print(" ### 시각화 ### ")
    elif menu == "2":
        print(" ### 데이터 처리 ### ")
    elif menu == "3":
        print(" ### 머신러닝 ### ")
    elif menu == "4":
        print(" ### 배포 ### ")
    else:
        print(" ### 해당 메뉴 없음 ### ")