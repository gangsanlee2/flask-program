class Member(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 회원관리 ### ")

    @staticmethod
    def print_menu():
        print("1. 회원 등록")
        print("2. 회원 출력")
        print("3. 회원 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 회원 등록 ### ")
            elif menu == 2:
                print(" ### 회원 목록 ### ")
            elif menu == 3:
                print(" ### 회원 삭제 ### ")
            else:
                print(" 다시 입력 ")

Member.main()