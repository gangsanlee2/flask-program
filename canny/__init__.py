'''
이미지 읽기의 flag는 3가지가 있습니다.

        cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
        cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
        cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다.

        3개의 flag대신에 1, 0, -1을 사용해도 됩니다.

Shape is (512, 512, 3)
Y축 : 512 (앞)
X축 : 512 (뒤)
3 : RGB(컬러) 로 되어있다는 뜻


cv2.waitKey(.) : keyboard입력을 대기하는 함수로 0이면 key입력까지 무한대기이며
                특정 시간동안 대기하려면 milisecond값을 넣어주면 됩니다.
cv2.destroyAllWindow() : 화면에 나타난 윈도우를 종료합니다. 일반적으로 위 3개는 같이 사용됩니다.
'''

from canny.views import MenuController
from util.common import Common
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import requests

class CannnyModel:
    pass


if __name__ == '__main__':
    Squid = 'squid.jpg'
    Messi = "https://docs.opencv.org/4.x/roi.jpg"
    Building = "http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
    menu_ctrl = MenuController()
    while True:
        menus = ["종료", "원본보기", "그레이스케일", "엣지검출",
                 "직선검출"]
        menu = Common.menu(menus)
        if menu == "0":
            menu_ctrl.menu_0(menus[0])
            break
        elif menu == "1":
            menu_ctrl.menu_1(menus[1], Squid)
        elif menu == "2":
            menu_ctrl.menu_2(menus[2], Messi)
        elif menu == "3":
            menu_ctrl.menu_3(menus[3], Messi)
        elif menu == "4":
            menu_ctrl.menu_4(menus[4], Building)
        else:
            print(" ### 해당 메뉴 없음 ### ")

'''
    print(f'cv2 버전 {cv2.__version__}') # cv2 버전 4.6.0
    a = cv2.imread('./data/Lenna.png', cv2.IMREAD_COLOR)
    print(f' Shape is {a.shape}')
    cv2.imshow('Gray', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
