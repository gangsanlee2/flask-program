'''
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오.
예) [12, 23, 48,...,]
사용자의 input 값이 12인 경우
출력값이 12, 48만 되도록 한다.
'''
from src.cmm.service.common import Common


class SearchNumber(object):

    def __init__(self):
        pass

    def execute(self):
        print(" ### 숫자찾기 ### ")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 숫자 등록 ### ")
            elif menu == 2:
                print(" ### 숫자 목록 ### ")
            elif menu == 3:
                print(" ### 숫자 삭제 ### ")
            else:
                print(" 다시 입력 ")

SearchNumber.main()