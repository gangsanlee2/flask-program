import cv2

from lenna.models import LennaModel
from util.dataset import Dataset


class LennaController(object):
    model = LennaModel()

    def __init__(self):
        pass

    def __str__(self):
        return ""

    def preprocess(self, fname) -> object:
        model = self.model
        img = model.new_model(fname)
        return img

    def modeling(self, fname) -> object:
        img = self.preprocess(fname)
        return img

if __name__ == '__main__':
    pass