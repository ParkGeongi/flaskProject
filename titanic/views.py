from titanic.models import TitanicModel
from util.dataset import Dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import  LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
class TitanicController(object):

    def __int__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self, train, test) -> object: #전처리

        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정

        this = model.sex_norminal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_norminal(this)
        this = model.title_norminal(this)
        this = model.drop_features(this,
                                   'PassengerId', 'Name', 'Sex', 'Age',
                                   'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin')
        return this

    def postprocess(self):
        pass

    def modeling(self, train, test)-> object: #모델 생성
        model =self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self,train,test):
        this = self.modeling(train,test)
        accuracy1 = self.model.get_accuracy(this ,DecisionTreeClassifier())
        #accuracy2 = self.model.get_accuracy(this, LogisticRegression())
        accuracy3 = self.model.get_accuracy(this, RandomForestClassifier())
        accuracy4 = self.model.get_accuracy(this, svm.SVC())
        print(f'DecisionTreeClassifier 알고리즘 정확도 : {accuracy1} %')
        #print(f'LogisticRegression 알고리즘 정확도 : {accuracy2} %')
        print(f'RandomForestClassifier 알고리즘 정확도 : {accuracy3} %')
        print(f'서포트 벡터 머신 알고리즘 정확도 : {accuracy4} %')


    def sumit(self):
        pass



if __name__ == '__main__':
    C = TitanicController()
    this = Dataset()
    #this = C.preprocess("train.csv","test.csv")
    #print(this.train.columns)
    #print(this.train.head())
    this = C.preprocess('train.csv', 'test.csv')
    print(this.train)
    print(this.test)