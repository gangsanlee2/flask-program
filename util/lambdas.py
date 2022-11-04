from PIL import Image

import cv2 as cv

def MosaicLambdas(cmd, target): #Command Pattern
    #cmd = params[0]
    #target = params[1]
    if cmd == 'IMAGE_READ':
        return (lambda x: cv.imread('./data/' + x))(target)
    elif cmd == 'GRAYSCALE':
        return (lambda x: cv.cvtColor(x, cv.COLOR_BGR2GRAY))(target)
    elif cmd == 'FROM_ARRAY':
        return (lambda x: Image.fromarray(x))(target)

