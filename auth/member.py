from util.common import Common


class Member(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 회원관리 ### ")


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
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