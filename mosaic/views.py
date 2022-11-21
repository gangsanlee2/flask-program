from matplotlib import pyplot as plt
from PIL import Image
from mosaic.services import ImageToNumberArray, Hough, Haar, Mosaic, Mosaics
import cv2 as cv
import numpy as np
import copy

from util.lambdas import MosaicLambdas


class MenuController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = MosaicLambdas('IMAGE_READ', params[1])
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
        #image = ExecuteLambda('IMAGE_READ', arr)
        plt.imshow(MosaicLambdas('FROM_ARRAY',arr))
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        ### 디스크에서 읽는 경우 ###
        # image = cv.imread('./data/roi.jpg', 0)
        # image = cv.imread(image, 0)
        ### 메모리에서 읽는 경우 ###
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        # image = GaussianBlur(image, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # image = Canny(image, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
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
        cat = MosaicLambdas("IMAGE_READ", params[1])
        mos = Mosaic(cat, (200,200,300,300), 10)
        cv.imwrite('./data/cat-mosaic.png', mos)
        cv.imshow("CAT MOSAIC", mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        print(params[0])

        girl = params[2]
        girl = MosaicLambdas("IMAGE_READ", girl)
        girl = cv.cvtColor(girl, cv.COLOR_BGR2RGB)
        girl_for_haar = copy.deepcopy(girl)
        gray = MosaicLambdas('GRAYSCALE',girl)
        edges = cv.Canny(np.array(girl), 100, 200)
        dst = Hough(edges)
        xml = params[1]
        rect = Haar(girl_for_haar, xml)
        girl_mosaic = Mosaic(girl, rect, 10)

        plt.subplot(161), plt.imshow(girl)
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(edges, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(dst, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(girl_for_haar)
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(girl_mosaic)
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])

        plt.show()

        #girl = cv.cvtColor(girl, cv.COLOR_RGB2BGR)
        #cv.imwrite('./data/girl-face.png', girl)

        #girl = cv.cvtColor(girl, cv.COLOR_RGB2BGR)
        #cv.imwrite('./data/girl-mosaic.png', girl)

    @staticmethod
    def menu_7(*params):
        print(params[0])
        with_mom = MosaicLambdas("IMAGE_READ", params[1])
        with_mom = cv.cvtColor(with_mom, cv.COLOR_RGB2BGR)
        with_mom_mosaics = Mosaics(with_mom, 10)

        plt.subplot(121), plt.imshow(with_mom)
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(with_mom_mosaics)
        plt.title('Mosaics'), plt.xticks([]), plt.yticks([])
        plt.show()

        '''
        cv.imshow("WITH MOM MOSAIC", with_mom_mosaics)
        cv.waitKey(0)
        cv.destroyAllWindows()
        cv.imwrite('./data/mosaics_with_mom.png', with_mom_mosaics)
        '''

    