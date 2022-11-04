from io import BytesIO
import cv2 as cv
import requests
from const.crawler import HEADERS
from util.dataset import Dataset
from PIL import Image

def Mosaic_Lambdas(*params):
    ds = Dataset()
    cmd = params[0]
    target = params[1]
    if cmd =='Disk_Img_Read':
        return (lambda x: cv.imread(ds.context  + x))(target)
    elif cmd == 'Memory_Img_Read':
        return (lambda x:Image.open(BytesIO(requests.get(x, headers=HEADERS).content)))(target)
    elif cmd == 'Gray':
        return (lambda img: img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229)(target)
    elif cmd =='Image_From_Array':
        return (lambda x: Image.fromarray(x))(target)

