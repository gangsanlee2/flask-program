class OddEven(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 홀짝구분 ### ")

    @staticmethod
    def print_menu():
        print("1. 홀짝 등록")
        print("2. 홀짝 출력")
        print("3. 홀짝 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = OddEven.print_menu()
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