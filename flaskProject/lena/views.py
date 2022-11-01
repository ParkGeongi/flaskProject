import cv2

from lena.models import LennaModel, CannyModel, Gray, Origin
import matplotlib.pyplot as plt
from util.dataset import Dataset
from PIL import Image

class LennaController(object):

    def __init__(self,url):
        self.url =url
        pass

    def __str__(self):
        return f""
    dataset = Dataset()

    def origin_img(self):
        url = self.url
        img = Origin(url).get()
        img = Image.fromarray(img)
        plt.imshow(img)
        plt.show()

    def canny_edge(self):
        url = self.url
        img = CannyModel(url).get()
        img = Image.fromarray(img)
        plt.imshow(img)
        plt.show()

    def gray_img(self):
        url = self.url
        img = Gray(url).get()
        img = Image.fromarray(img)
        plt.imshow(img)
        plt.show()


    def preprocess(self, fname) -> object:  # 전처리
        img = self.model.new_model(fname)
        return img

    def modeling(self, fname) -> object:
        img = self.preprocess(fname)
        return img

    def learning(self):  # 기계학습
        pass

    def submit(self):  # 배포
        pass


if __name__ == "__main__":
    pass