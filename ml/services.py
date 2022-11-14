import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from util.dataset import Dataset

'''def execute():
    clf = RandomForestClassifier(random_state= 0)
    X = [[1,2,3],[11,12,13]] # 샘플 2, 피쳐 3 / 확률변수
    y = [0,1] # E: 각 샘플의 클래스(타겟의 클래스 값) /  기대값, 예측값
    clf.fit(X,y) # clf 객체를 통해 학습
    print(clf.predict([[4,5,6],[14,15,16]])) # 새로운 데이터셋의 클래스 추정
'''
class StrokeModel(object):
    dataset = Dataset()
    def __init__(self):
        pass
    def __str__(self):
        pass

    def new_model(self,fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows',None)
        df = pd.read_csv(this.context + this.fname)
        return df

    def target(self,df):
        print('결측값 확인 : '+ str(df['stroke'].isnull().sum()) + '\n')
        print('뇌졸증 경험 여부 : ' + str(df['stroke'].value_counts(dropna=False))+ '\n')
        print('비율 : ' + str(df['stroke'].value_counts(dropna=False,normalize=True)))

    def processong(self, df):
        cols = ['age','avg_glucose_level','bmi']
        print("data type : " + str(df[cols].dtypes))
        pd.options.display.float_format= '{:.2f}'.format
        print(df[cols].describe())

        c = df['age'] > 18
        print(df[c].head(3))
        print(len(df[c]))

        print(len(df[c]) / len(df))
        df1= df[c]
        df1 = df1.rename(columns = {'Residence_type' : 'residence_type'})
        cols1 = ['gender','hypertension','heart_disease','ever_married',
                 'work_type','residence_type','smoking_status']
        print(df1[cols1].isnull().sum())
        print(df1[cols1].dtypes)
