class Person(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 자기소개 ### ")

    @staticmethod
    def print_menu():
        print("1. 자기소개 등록")
        print("2. 자기소개 출력")
        print("3. 자기소개 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 자기소개 등록 ### ")
            elif menu == 2:
                print(" ### 자기소개 목록 ### ")
            elif menu == 3:
                print(" ### 자기소개 삭제 ### ")
            else:
                print(" 다시 입력 ")

Person.main()