'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''


class Contacts(object):

    def __init__(self, name, tel, email, adress):
        self.name = name
        self.tel = tel
        self.email = email
        self.adress = adress

    def __str__(self):
        return f"{self.name} {self.tel} {self.email} {self.adress}"

    @staticmethod
    def result(ls):
        print(" ### 주소록 ### ")
        print("****************************")
        print("이름   전화번호    이메일 주소")
        print("****************************")
        [print(i) for i in ls]
        print("****************************")

    @staticmethod
    def delete(ls, name):
        for i,j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def new_contacts():
        return Contacts(input(" 이름 : "), input(" 전화번호 : "),
                        input(" 이메일 : "), input(" 주소 : "))

