from user.bmi import Bmi
from user.contacts import Contacts
from user.grade import Grade
from user.person import Person
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료", "bmi", "주소록", "성적","자기소개"])
    if menu == 0:
        print(" ### 종료 ### ")
        break
    elif menu == 1:
        print(" ### bmi ###")
        submenu = Common.menu(["종료","등록","목록","삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Bmi.new_bmi())
        elif submenu == 2:
            Bmi.result(ls)
        elif submenu == 3:
            name = input(" 삭제할 이름 : ")
            Bmi.delete(ls, name)
        else:
            print(" 다시 입력 ")
    elif menu == 2:
        print(" ### 주소록 ###")
        submenu = Common.menu(["종료","등록","목록","삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Contacts.new_contacts())
        elif submenu == 2:
            Contacts.result(ls)
        elif submenu == 3:
            name = input(" 삭제할 이름 : ")
            Contacts.delete(ls, name)
        else:
            print(" 다시 입력 ")
    elif menu == 3:
        print(" ### 성적 ###")
        submenu = Common.menu(["종료","등록","목록","삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Grade.new_grade())
        elif submenu == 2:
            Grade.result(ls)
        elif submenu == 3:
            name = input(" 삭제할 이름 : ")
            Grade.delete(ls,name)
        else:
            print(" 다시 입력 ")
    elif menu == 4:
        print(" ### 자기소개 ###")
        submenu = Common.menu(["종료","등록","목록","삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Person.new_person())
        elif submenu == 2:
            Person.result(ls)
        elif submenu == 3:
            name = input(" 삭제할 이름 : ")
            Person.delete(ls,name)
        else:
            print(" 다시 입력 ")
    else:
        print(" 다시 입력 ")