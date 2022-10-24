class Calculator(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 계산기 ### ")

    @staticmethod
    def print_menu():
        print("1. 계산결과 등록")
        print("2. 계산결과 출력")
        print("3. 계산결과 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
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