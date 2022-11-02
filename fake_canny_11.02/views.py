from io import BytesIO
import requests

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from services import CannyModel, image_read

class MenuController(object):

    @staticmethod
    def menu_0(param):
        print(param)

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = image_read(params[1])
        cv2.imshow('Original', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
        img = Image.fromarray(img)
        plt.imshow(img)
        plt.show()
        '''

    @staticmethod
    def menu_2(*params):
        print(params[0])
        img = CannyModel(params[1])
        img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(img)

        plt.imshow(Image.fromarray(img))
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        img = CannyModel(params[1])
        print(f'img type : {type(img)}')
        edges = cv2.Canny(img, 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])

        img = CannyModel(params[1])
        edges = cv2.Canny(img, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180., 120, minLineLength=50, maxLineGap=5)
        dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

        '''
        img = Image.fromarray(dst)
        plt.imshow(img)
        plt.show()
        '''

        cv2.imshow('Lines', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == '__main__':
    pass