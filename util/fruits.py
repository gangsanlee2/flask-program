class Fruits(object):

    def __init__(self, name, won):
        self.name = name
        self.won = won

    def return_info(self):
        return f"{self.name} {self.won}"

    @staticmethod
    def print_result(ls):
        print(" ### 과일가게 ### ")
        print("***************************")
        print("이름   가격")
        for i in ls:
            print(i.return_info())
        print("***************************")

    @staticmethod
    def new_fruits():
        return Fruits(input(" 이름 : "), int(input(" 가격 : ")))

    @staticmethod
    def print_menu():
        print("1. 과일가게 등록")
        print("2. 과일가게 출력")
        print("3. 과일가게 삭제")
        print("0. 종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Fruits.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 과일가게 등록 ### ")
                ls.append(Fruits.new_fruits())
            elif menu == 2:
                print(" ### 과일가게 목록 ### ")
                Fruits.print_result(ls)
            elif menu == 3:
                print(" ### 과일가게 삭제 ### ")
            else:
                print(" 다시 입력 ")

Fruits.main()