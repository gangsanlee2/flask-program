"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
유관순 90 90 92 272 90.6 A
********************************
"""

class Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.set_total()
        self.set_avg()
        self.set_grade()

    def set_total(self):
        self.total = self.math + self.kor + self.eng

    def set_avg(self):
        self.avg = self.total/3

    def set_grade(self):
        pass

    def return_info(self):
        return f"{self.name} {self.kor} {self.eng} {self.math} " \
               f"{self.total} {self.avg} {self.grade}"

    @staticmethod
    def print_result(ls):
        print("### 성적표 ###")
        print("********************************")
        print("이름 국어 영어 수학 총점 평균 학점")
        print("*******************************")
        for i in ls:
            print(i.return_info())
        print("*******************************")

    @staticmethod
    def new_grade():
        return Grade(input(" 이름 : "), int(input(" 국어 : ")),
                     int(input(" 영어 : ")), int(input(" 수학 : ")))

    @staticmethod
    def print_menu():
        print("1. 성적표 등록")
        print("2. 성적표 출력")
        print("3. 성적표 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 성적표 등록 ###")
                ls.append(Grade.new_grade())
            elif menu == 2:
                print(" ### 성적표 목록 ###")
                Grade.print_result(ls)
            elif menu == 3:
                print(" ### 성적표 삭제 ###")
            else:
                print(" 다시 입력 ")

Grade.main()