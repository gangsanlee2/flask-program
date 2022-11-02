from io import BytesIO

import cv2
import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class LennaModel(object):

    def __init__(self):
        '''
        headers = {'User-Agent': 'My User Agent 1.0'}
        res = requests.get("https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png", headers=headers)
        fake_canny_11.02. = Image.open(BytesIO(res.content))
        self.fake_canny_11.02. = np.array(fake_canny_11.02.)
        self.createOption()
        '''

    def __str__(self):
        return ""

    def new_model(self, fname) -> object:
        context = './data/'
        this = cv2.imread(context + fname, cv2.IMREAD_COLOR)
        return this

    def createOption(self):
        self.ADAPTIVE_THRESH_MEAN_C = 0
        self.ADAPTIVE_THRESH_GAUSSIAN_C = 1
        self.THRESH_BINARY = 2
        self.THRESH_BINARY_INV = 3

    def imshow(self, this):
        this = Image.fromarray(this)
        plt.imshow(this)
        plt.show()

    def gray_scale(self, this):
        dst = this[:, :, 0] * 0.114 + this[:, :, 1] * 0.587 + this[:, :, 2] * 0.229
        return dst

if __name__ == '__main__':
    lm = LennaModel()
    this = lm.gray_scale(lm.lenna)
    lm.imshow(this)