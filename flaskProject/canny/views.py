import cv2
import numpy as np
from io import BytesIO
import canny
import requests
import canny.survises as models
from canny.survises import Origin,Gray,Canny,image_read
import matplotlib.pyplot as plt
from util.dataset import Dataset
from PIL import Image
from const.crawler import HEADERS
class LennaController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f""
    @staticmethod
    def Origin(*params):
        print(f" ### {params[1]} ### ")

        img = Origin(Image.open(BytesIO(requests.get(params[0], headers=HEADERS).content)))
        (lambda x : plt.imshow(Image.fromarray(x)))(img)
        plt.show()

    @staticmethod
    def CannyMemory(*params):
        print(f" ### {params[1]} ### ")
        url = np.array(Image.open(BytesIO(requests.get(params[0], headers=HEADERS).content)))
        (lambda x : plt.imshow(Image.fromarray(x)))(Canny(url))
        plt.show()

    @staticmethod
    def CannyDisk(*params):
        print(f" ### {params[1]} ### ")
        img = np.array(image_read(params[0]))
        (lambda x: plt.imshow(Image.fromarray(x)))(Canny(img))
        plt.show()

    @staticmethod
    def Gray(*params):
        print(f" ### {params[1]} ### ")
        img = Gray(Image.open(BytesIO(requests.get(params[0], headers=HEADERS).content)))
        (lambda x : plt.imshow(Image.fromarray(x)))(img)
        plt.show()

