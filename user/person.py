"""
이름, 주민번호 (950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
"""

class Person(object):

    def __init__(self, name, num, adress):
        self.name = name
        self.age = 0
        self.num = num
        self.sex = ""
        self.adress = adress

    def __str__(self):
        return f"{self.name} {self.age} {self.num} {self.sex} {self.adress}"

    def set_age(self):
        current = 2022
        year = int(self.num[:2]) #인덱스 0,1은 출생년도
        sex_checker = int(self.num[6]) #7은 성별판별번호 인덱스
        if sex_checker == 1 or sex_checker == 2:
            year += 1900
            if sex_checker == 1:
                self.sex = "남성"
            else:
                self.sex = "여성"
        elif sex_checker == 3 or sex_checker == 4:
            year += 2000
            if sex_checker == 3:
                self.sex = "남성"
            else:
                self.sex = "여성"
        self.age = current - year

    @staticmethod
    def result(ls):
        print(" ### 자기소개어플 ### ")
        print("*********************************")
        print(" 이름  나이  성별  주소  ")
        [print(i) for i in ls]
        print("*********************************")

    @staticmethod
    def new_person():
        return Person(input(" 이름 : "), input(" 주민번호 : "), input(" 주소 : "))
