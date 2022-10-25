from store.fruits import Fruits
from util.common import Common

ls = []
while True:
    menu = Common.menu()
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