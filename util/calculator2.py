class Calculator():

    def __init__(self):
        pass

    def excute(self):
        print(" ### 계산기 ### ")

    @staticmethod
    def print_menu():
        print("1. 계산결과 등록")
        print("2. 계산결과 목록")
        print("3. 계산결과 삭제")
        print("0. 종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()


Calculator.main()