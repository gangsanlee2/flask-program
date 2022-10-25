from util.common import Common


class Fruits(object):

    def __init__(self, name, won):
        self.name = name
        self.won = won

    def __str__(self):
        return f"{self.name} {self.won}"

    @staticmethod
    def print_result(ls):
        print(" ### 과일가게 ### ")
        print("***************************")
        print("이름   가격")
        print("***************************")
        for i in ls:
            print(i)
        print("***************************")

    @staticmethod
    def new_fruits():
        return Fruits(input(" 이름 : "), int(input(" 가격 : ")))
