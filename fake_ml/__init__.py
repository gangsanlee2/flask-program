from fake_ml.views import StrokeController
from util.common import Common
CSV = 'healthcare-dataset-stroke-data.csv'

if __name__ == '__main__':
    api = StrokeController()
    while True:
        print("*"*100)
        menu = Common.menu(["종료", "문제제기", "데이터구하기", "타깃변수설정", "데이터처리","시각화","모델링","실행","학습","예측"])
        print("*" * 100)
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 문제제기 ### ")
        elif menu == "2":
            print(" ### 데이터구하기 ### ")
            api.set_data(CSV)
        elif menu == "3":
            print(" ### 타깃변수설정 ### ")
        elif menu == "4":
            print(" ### 데이터처리 ### ")
        elif menu == "5":
            print(" ### 시각화 ### ")
        elif menu == "6":
            print(" ### 모델링 ### ")
        elif menu == "7":
            print(" ### 실행 ### ")
        elif menu == "8":
            print(" ### 학습 ### ")
        elif menu == "9":
            print(" ### 예측 ### ")
        else:
            print(" ### 해당 메뉴 없음 ### ")