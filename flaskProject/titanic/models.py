import numpy as np
import pandas as pd

# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
# =============null========================
# Age            177
# Cabin          687
# Embarked         2

from util.dataset import Dataset
class TitanicModel(object):

    dataset = Dataset()

    def __int__(self):
        pass

    def __str__(self):

        df = self.new_model(fname = self.dataset.fname)

        return f"{type(df)}\n {df.columns}\n {df.head()}\n {df.isnull().sum()}"

    def preprocess(self) :
        pass

    def new_model(self,fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname #setter
        df = pd.read_csv(this.context + this.fname)
        return df #객체화 시킨것

    @staticmethod
    def creat_train(this)-> object:

        return this




    def creat_label(self): #test

        pass
