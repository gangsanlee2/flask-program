from user import Bmi, Contacts, Grade, Person
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료","bmi","주소록","성적","자기소개"])
    if menu == 0: break
    elif menu == 1:
        print(" ### bmi ### ")
        submenu = Common.menu(["종료","bmi 등록","bmi 목록","bmi 삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Bmi.new_bmi())
        elif submenu == 2:
            Bmi.result(ls)
        elif submenu == 3:
            Bmi.delete(ls,input(" 삭제할 이름 : "))
        else:
            print(" 다시 입력 ")
    elif menu == 2:
        print(" ### 주소록 ### ")
        submenu = Common.menu(["종료","주소 등록","주소 목록","주소 삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Contacts.new_contacts())
        elif submenu == 2:
            Contacts.result(ls)
        elif submenu == 3:
            Contacts.delete(ls,input(" 삭제할 이름 : "))
        else:
            print(" 다시 입력 ")
    elif menu == 3:
        print(" ### 성적 ### ")
        submenu = Common.menu(["종료","성적 등록","성적 목록","성적 삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Grade.new_grade())
        elif submenu == 2:
            Grade.result(ls)
        elif submenu == 3:
            Grade.delete(ls,input(" 삭제할 이름 : "))
        else:
            print(" 다시 입력 ")
    elif menu == 4:
        print(" ### 자기소개 ### ")
        submenu = Common.menu(["종료","자기소개 등록","자기소개 목록","자기소개 삭제"])
        if submenu == 0: break
        elif submenu == 1:
            ls.append(Person.new_person())
        elif submenu == 2:
            Person.result(ls)
        elif submenu == 3:
            Person.delete(ls,input(" 삭제할 이름 : "))
        else:
            print(" 다시 입력 ")
    else:
        print(" 다시 입력 ")