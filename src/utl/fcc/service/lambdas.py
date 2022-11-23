from io import BytesIO
import cv2 as cv

import requests
from PIL import Image
from src.cmm.const.crawler import HEADERS
from src.cmm.const.path import CTX


def Mosaic_Lambdas(*params):

    cmd = params[0]
    target = params[1]
    if cmd =='Disk_Img_Read':
        return (lambda x: cv.imread(CTX + x))(target)
    elif cmd == 'Memory_Img_Read':
        return (lambda x: Image.open(BytesIO(requests.get(x, headers=HEADERS).content)))(target)
    elif cmd == 'Gray':
        return (lambda img: img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229)(target)
    elif cmd =='Image_From_Array':
        return (lambda x: Image.fromarray(x))(target)
