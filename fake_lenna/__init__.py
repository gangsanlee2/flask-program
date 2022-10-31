import cv2

from fake_lenna.views import LennaController
from util.common import Common

if __name__ == '__main__':
    while True:
        menu = Common.menu(["close", "show original"])
        if menu == "0":
            print(" ### close ### ")
            break
        elif menu == "1":
            print(" ### show original ### ")
            c = LennaController()
            this = c.modeling('Lenna.png')
            print(f'Shape is {this.shape}')
            cv2.imshow('Gray', this)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(" ### error ### ")

'''
a = cv2.imread('./data/Lenna.png', cv2.IMREAD_COLOR)
print(f'Shape is {a.shape}')
cv2.imshow('Gray', a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''