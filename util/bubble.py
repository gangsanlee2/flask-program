class Bubble(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 버블정렬 ### ")

    @staticmethod
    def print_menu():
        print("1. 버블정렬 등록")
        print("2. 버블정렬 출력")
        print("3. 버블정렬 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bubble.print_menu()
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