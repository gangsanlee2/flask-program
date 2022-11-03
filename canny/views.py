from matplotlib import pyplot as plt
from PIL import Image
from canny.services import ImageToNumberArray, ExecuteLambda, Hough, HaarCascade
import cv2 as cv
import numpy as np

class MenuController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = ExecuteLambda('IMAGE_READ', params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
        #img = ExecuteLambda('IMAGE_READ', arr)
        plt.imshow(ExecuteLambda('FROMARRAY',arr))
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        ### 디스크에서 읽는 경우 ###
        # img = cv.imread('./data/roi.jpg', 0)
        # img = cv.imread(img, 0)
        ### 메모리에서 읽는 경우 ###
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        # img = GaussianBlur(img, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # img = Canny(img, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])

        girl = params[2]
        girl = ExecuteLambda("IMAGE_READ", girl)
        girl = cv.cvtColor(girl, cv.COLOR_BGR2RGB)

        gray = ExecuteLambda('GRAYSCALE',girl)

        edges = cv.Canny(np.array(girl), 10, 100)

        dst = Hough(edges)

        plt.subplot(151), plt.imshow(girl)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        xml = params[1]
        HaarCascade(girl, xml)

        plt.subplot(152), plt.imshow(gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(edges, cmap='gray')
        plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(dst, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(girl)
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()

        girl = cv.cvtColor(girl, cv.COLOR_RGB2BGR)
        cv.imwrite('./data/girl-face.png', girl)

    @staticmethod
    def menu_6(*params):
        print(params[0])
