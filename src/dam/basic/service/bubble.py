from src.cmm.service.common import Common


class Bubble(object):

    def __init__(self):
        pass

    def __str__(self):
        print(" ### 버블정렬 ### ")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 버블정렬 등록 ### ")
            elif menu == 2:
                print(" ### 버블정렬 목록 ### ")
            elif menu == 3:
                print(" ### 버블정렬 삭제 ### ")
            else:
                print(" 잘못된 메뉴값, 다시 입력 ")

Bubble.main()