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
from util.common import Common


class Bmi(object):

    def __init__(self, name, cm, kg): #__init__ == Bmi  단지 동어 반복을 피하기 위해. 고로 Bmi(~~): 생성자
        self.name = name
        self.cm = cm
        self.kg = kg

    def __str__(self):
        return f"{self.name} {self.cm} {self.kg} 정상"

    @staticmethod
    def result(ls):
        print(" ### 비만도 계산 ### ")
        print("***************************")
        print("이름 키(cm) 몸무게(kg) 비만도")
        print("***************************")
        [print(i) for i in ls]
        print("***************************")

    @staticmethod
    def delete(ls, name):
        '''for i,j in enumerate(ls):
            if j.name == name:
                del ls[i]'''
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def new_bmi():
        return Bmi(input(" 이름 : "),
                    int(input(" 키 : ")),
                    int(input(" 몸무게 : ")))

