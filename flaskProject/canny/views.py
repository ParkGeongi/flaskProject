import cv2 as cv
import numpy as np
from io import BytesIO
import canny
import requests

from canny.survises import Origin, Gray, Canny, HoughLines, ExecuteLambda, Haar
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
    def Menu_1_Origin(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(ExecuteLambda('Memory_Img_Read', params[1]))
        plt.imshow(ExecuteLambda('Image_From_Array', img))
        plt.show()

    @staticmethod
    def Menu_2_Gray(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(ExecuteLambda('Memory_Img_Read', params[1]))
        img = ExecuteLambda('Gray',img)
        plt.imshow(ExecuteLambda('Image_From_Array',img))

        plt.show()

    @staticmethod
    def Menu_3_CannyDisk(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(ExecuteLambda('Disk_Img_Read',params[1]))
        (lambda x: plt.imshow(Image.fromarray(x)))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_4_CannyMemory(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(ExecuteLambda('Memory_Img_Read', params[1]))
        (lambda x : plt.imshow(Image.fromarray(x)))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_5_Hough(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(ExecuteLambda('Memory_Img_Read', params[1]))
        edges =  cv.Canny(img, 100, 200) # img, threshold 1, 2 \
        dst = HoughLines(edges)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_6_Haar(*params):
        print(f" ### {params[0]} ### ")
        haar = cv.CascadeClassifier(params[1])
        girl = params[2]
        # bgr -> rgb
        img1 = cv.cvtColor(Origin(ExecuteLambda('Disk_Img_Read',girl)), cv.COLOR_BGR2RGB)
        img2 = Gray(np.array(ExecuteLambda('Disk_Img_Read',girl)))
        img3 =Canny(np.array(ExecuteLambda('Disk_Img_Read',girl)))
        img4 = HoughLines(img3)

        plt.subplot(151), plt.imshow(img1)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(152), plt.imshow(img2,cmap = 'gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(img3,cmap = 'gray')
        plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(img4)
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])

        girl = Haar(img1, haar)

        plt.subplot(155), plt.imshow(girl)
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()

        #girl = cv.cvtColor(img1, cv.COLOR_RGB2BGR)
        #girl = cv.resize(girl, (300, 300))
        #cv.imwrite('girl_facing.png',girl)
        #cv.imshow('GIRL FACE',girl)
        #cv.waitKey(0)
        #cv.destroyWindow()


    def Menu_7_Mosaic(*params):
        print(f" ### {params[0]} ### ")




