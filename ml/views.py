import pandas as pd

from ml.services import StrokeModel

model =StrokeModel()
class StrokeController:


    def __init__(self):
        pass

    def __str__(self):
        pass

    def set_data(self,fname):
        print(model.new_model(fname).head(3))

    def create_target(self,fname):
        df = model.new_model(fname)
        model.target(df)
    def data_processing(self,fname):
        df = model.new_model(fname)
        model.processong(df)