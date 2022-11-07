class SearchNumber(object):

    def __init__(self):
        pass

    def excute(self):
        print(" ### 숫자 찾기 ### ")

    @staticmethod
    def print_menu():
        print("1. 숫자 등록")
        print("2. 숫자 목록")
        print("3. 숫자 삭제")
        print("0. 종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = SearchNumber.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 숫자 등록 ###")
            elif menu == 2:
                print(" ### 숫자 목록 ###")
            elif menu == 3:
                print(" ### 숫자 삭제 ###")
            else:
                print(" 다시 입력 ")

SearchNumber.main()