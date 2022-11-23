import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt


from src.cmm.com.service.dataset import Dataset
from src.dam.computer_vision.service.mosaic import Canny, HoughLines, Haar, Mosaic, Mosaic_People, Origin, Gray
from src.utl.fcc.service.lambdas import Mosaic_Lambdas
from PIL import Image


class MenuController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f""

    @staticmethod
    def Menu_1_Origin(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        plt.imshow(Mosaic_Lambdas('Image_From_Array', img))
        plt.show()
        print(f' cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')


    @staticmethod
    def Menu_2_Gray(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        img = Mosaic_Lambdas('Gray',img)
        plt.imshow(Mosaic_Lambdas('Image_From_Array',img))
        plt.show()

    @staticmethod
    def Menu_3_CannyDisk(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Disk_Img_Read',params[1]))
        (lambda x: plt.imshow(x))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_4_CannyMemory(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        (lambda x : plt.imshow(Image.fromarray(x)))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_5_Hough(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
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
        img1 = Mosaic_Lambdas('Disk_Img_Read',girl)
        girl,rect = Haar(img1, haar)
        plt.subplot(111), plt.imshow(girl)
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_7_Mosaic_Cat(*params):
        print(f" ### {params[0]} ### ")
        cat = cv.imread(f'{Dataset().context}{params[1]}')
        mos = Mosaic(cat,(150,150,450,450), 10)
        cv.imwrite(f'{Dataset().context}cat-mosaic.png',mos)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_8_Mosaic_Girl(*params):
        print(f" ### {params[0]} ### ")
        haar = cv.CascadeClassifier(params[1])
        girl = params[2]
        img = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', girl), cv.COLOR_BGR2RGB)
        img1 = img.copy()
        girl,rect = Haar(img, haar)
        mos = Mosaic(img1,rect, 10)
        cv.imwrite(f'{Dataset().context}girl-mosaic.png', mos)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_9_Mosaic_Two(*params):
        print(f" ### {params[0]} ### ")
        haar = params[1]
        girl = params[2]

        img = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', girl), cv.COLOR_BGR2RGB)

        mos =Mosaic_People(img,10, haar)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def Menu_10_All_View(*params):

        print(f" ### {params[0]} ### ")
        haar = params[1]
        img = params[2]
        img_people = params[3]


        img1 = cv.cvtColor(Origin(Mosaic_Lambdas('Disk_Img_Read',img)), cv.COLOR_BGR2RGB) # bgr -> rgb

        img_copy = img1.copy()
        img2 = Gray(np.array(Mosaic_Lambdas('Disk_Img_Read',img)))

        img3 =Canny(np.array(Mosaic_Lambdas('Disk_Img_Read',img)))

        img4 = HoughLines(img3)

        img5,rect = Haar(img1, cv.CascadeClassifier(haar))

        mos = Mosaic_People(img_copy,10,haar) #img, size, haar경로

        #mos_two = Mosaic_People(Mosaic_People(cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', img_people), cv.COLOR_BGR2RGB), 10, haar),10,haar)# harr경로를 받아서 servise에서 처리함

        img_people = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', img_people), cv.COLOR_BGR2RGB)
        mos_img = Mosaic_People(Mosaic_People(img_people, 10, haar),10,haar)




        plt.subplot(331), plt.imshow(img_copy)
        plt.title('Original '), plt.xticks([]), plt.yticks([])
        plt.subplot(332), plt.imshow(img2, cmap='gray')
        plt.title('Gray '), plt.xticks([]), plt.yticks([])
        plt.subplot(333), plt.imshow(img3, cmap='gray')
        plt.title('Canny '), plt.xticks([]), plt.yticks([])
        plt.subplot(334), plt.imshow(img4)
        plt.title('Hough '), plt.xticks([]), plt.yticks([])
        plt.subplot(335), plt.imshow(img5)
        plt.title('Haar '), plt.xticks([]), plt.yticks([])
        plt.subplot(336), plt.imshow(mos)
        plt.title('Mosaic '), plt.xticks([]), plt.yticks([])
        plt.subplot(337), plt.imshow(mos_img)
        plt.title('Mosaic '), plt.xticks([]), plt.yticks([])
        plt.show()
        #girl = cv.cvtColor(img1, cv.COLOR_RGB2BGR)
        #girl = cv.resize(girl, (300, 300))
        #cv.imwrite('girl_facing.png',girl)
        #cv.imshow('GIRL FACE',girl)
        #cv.waitKey(0)
        #cv.destroyWindow()


