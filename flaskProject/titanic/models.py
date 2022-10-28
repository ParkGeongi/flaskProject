import numpy as np
import pandas as pd



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


    ''' Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

   # =============null========================
   # Age            177
   # Cabin          687
   # Embarked         2
   #시각화를 통해 얻은 상관관계 변수 (variable = feature = column)는
    Survived 와 밑에 것들 관계
   # Pclass
   # Sex
   # Age
   # Fare
   # Embarked
   '''

    @staticmethod
    def creat_train(this)-> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def creat_label(this) -> object:
        return this.train['Survived']


    @staticmethod
    def drop_features(this,*feature) -> object: # * 자료구조 라는 뜻
        for i in feature:
            this.train = this.train.drop(i, axis =1)
            this.test = this.test.drop(i, axis =1)
        return this

    #def pclass_ordinal(this) ->object: #1등칸 2등칸 3등칸
      #return this 할 필요없다. ordinal, 1 2 3 중 하나로 나오기 때문에

    @staticmethod
    def sex_nominal(this)->object: # male -> 0 female -> 1
        #gender_mapping = {"male" : 0 , "female" : 1} # mapping은 dic
        for i in [this.train,this.test]:
            i['Gender'] = i['Sex'].map({"male" : 0 , "female" : 1})

        return this

    @staticmethod
    def age_ordinal(this)->object: # 연령대 10대 20대 30대



        return this

    @staticmethod
    def fare_ordinal(this)->object: # 4등분 pd.qcut 1이 가장 작은 요금 4가 가장 높은 요금
        for i in [this.train,this.test]:
            i['FareBand'] = pd.qcut(i['Fare'],4,labels=['1', '2', '3','4'])
        return this

    @staticmethod
    def embarked_nominal(this)->object: # 승선 항구 C Q S
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        for i in [this.train,this.test]:
            i['Embarked'] = i['Embarked'].map({'S' : 1, 'C' :2, 'Q': 3})
        return this


if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model("train.csv")
    this.test = t.new_model("test.csv")
    this = TitanicModel.sex_nominal(this)
    this = TitanicModel.fare_ordinal(this)
    this = TitanicModel.embarked_nominal(this)
    print(this.train['FareBand'])
    print(this.train['Gender'])
    print(this.train['Embarked'])
    print(this.train.head())



