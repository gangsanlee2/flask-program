from src.cmm.service.common import Common


class Calculator(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 계산기 ### ")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
            if menu == 1:
                print(" ### 계산결과 등록 ### ")
            elif menu == 2:
                print(" ### 계산결과 목록 ### ")
            elif menu == 3:
                print(" ### 계산결과 삭제 ### ")
            elif menu == 0:
                print(" ### 종료 ### ")
                break
            else:
                print(" 다시 입력 ")

Calculator.main()