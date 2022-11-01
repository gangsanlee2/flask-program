import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import requests
from PIL import Image
from io import BytesIO



headers = {'User-Agent': 'My User Agent 1.0'}
res = requests.get("https://docs.opencv.org/4.x/roi.jpg", headers=headers)
messi = Image.open(BytesIO(res.content))

img = cv.imread(messi,0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()