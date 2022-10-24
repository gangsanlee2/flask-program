class RandomList(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 랜덤리스트 ### ")

    @staticmethod
    def print_menu():
        print("1. 랜덤리스트 등록")
        print("2. 랜덤리스트 출력")
        print("3. 랜덤리스트 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = RandomList.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 랜덤리스트 등록 ### ")
            elif menu == 2:
                print(" ### 랜덤리스트 목록 ### ")
            elif menu == 3:
                print(" ### 랜덤리스트 삭제 ### ")
            else:
                print(" 다시 입력 ")

RandomList.main()