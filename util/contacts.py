class Contacts(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 주소록 ### ")

    @staticmethod
    def print_menu():
        print("1. 주소록 등록")
        print("2. 주소록 출력")
        print("3. 주소록 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contacts.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 주소록 등록 ### ")
            elif menu == 2:
                print(" ### 주소록 목록 ### ")
            elif menu == 3:
                print(" ### 주소록 삭제 ### ")
            else:
                print(" 다시 입력 ")

Contacts.main()
