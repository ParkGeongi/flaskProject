from titanic.models import TitanicModel
from util.dataset import Dataset

class TitanicController(object):

    def __int__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()
    def mining(self):
        pass

    def preprocess(self, train, test) -> object: #전처리

        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정

        this = model.pclass_ordinal(this)
        this = model.sex_nominal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)

        return this

    def postprocess(self):
        pass

    def modeling(self, train, test)-> object: #모델 생성
        model =self.model
        this = self.preprocess(train, test)
        this.label = model.creat_label(this)
        this.train = model.creat_train(this)
        return this

    def learning(self):
        pass

    def sumit(self):
        pass







