'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
이순신 170 79 정상
유관순 170 79 정상
***************************
'''

class Bmi(object):

    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    def return_info(self):
        return f"{self.name} {self.cm} {self.kg} 정상"

    @staticmethod
    def print_result(ls):
        print(" ### 비만도 계산 ### ")
        print("***************************")
        print("이름 키(cm) 몸무게(kg) 비만도")
        print("***************************")
        for i in ls:
            print(i.return_info())
        print("***************************")

    @staticmethod
    def new_bmi():
        return Bmi(input(" 이름 : "),
                    int(input(" 키 : ")),
                    int(input(" 몸무게 : ")))


    @staticmethod
    def print_menu():
        print("1. 비만지수 등록")
        print("2. 비만지수 출력")
        print("3. 비만지수 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 비만지수 등록 ### ")
                ls.append(Bmi.new_bmi())
            elif menu == 2:
                print(" ### 비만지수 목록 ### ")
                Bmi.print_result(ls)
            elif menu == 3:
                print(" ### 비만지수 삭제 ### ")
            else:
                print(" 잘못된 메뉴값. 다시 입력 ")

Bmi.main()