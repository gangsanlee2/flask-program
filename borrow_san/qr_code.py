# QR 생성 코드
# pip install pyqrcode
import pyqrcode


def creat_QR():
    link = 'https://docs.google.com/document/d/1UI2QaWFm0-UjIoTsR_y5BGFa-U1nLqGAf-6F3zsr1Sk/edit#'
    qr = pyqrcode.create(link)
    qr.png('./save/qr-ran.png')


if __name__ == '__main__':
    creat_QR()