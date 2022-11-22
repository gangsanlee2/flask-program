from src.cmm.service.common import Common


class RandomList(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 랜덤리스트 ### ")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
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