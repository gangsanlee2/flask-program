from src.cmm.service.common import Common


class OddEven(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 홀짝구분 ### ")


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 홀짝 등록 ### ")
            elif menu == 2:
                print(" ### 홀짝 목록 ### ")
            elif menu == 3:
                print(" ### 홀짝 삭제 ### ")
            else:
                print(" 다시 입력 ")

OddEven.main()