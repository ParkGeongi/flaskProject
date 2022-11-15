import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
OKLAHOMA_MENUS = ["종료", #0
                "데이터구조파악",#1
                "변수한글화",#2
                "연속형변수편집",#3 18세이상만 사용함
                "범주형변수편집",#4
                "타겟",#5
                "파티션",#6
                "모델링",#7
                "학습",#8
                "예측"]#9
oklahoma_meta = {

'AGEP' : '나이',
'BDSP' : '침실 수',
'ELEP' : '월 전기료',
'GASP' : '월 가스비',
'HINCP' : '가계 소득',
'NRC' : '자녀 수',
'RMSP' : '방 수',
'VALP' : '주택 가격',


}
oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.norminal_variables(),
    "5" : lambda t: t.target(),
    "6" : lambda t: t.partition(),
    "7" : lambda t: t.modeling(),
    "8" : lambda t: t.learning(),
    "9" : lambda t: t.predict()

}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21395 entries, 0 to 21394
Data columns (total 32 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   ACCESS   21395 non-null  float64
 1   ACR      21395 non-null  float64
 2   AGEP     21395 non-null  int64  
 3   BATH     21395 non-null  float64
 4   BDSP     21395 non-null  float64
 5   BLD      21395 non-null  float64
 6   CONP     21395 non-null  float64
 7   COW      12111 non-null  float64
 8   ELEP     21395 non-null  float64
 9   FESRP    21395 non-null  int64  
 10  FKITP    21395 non-null  float64
 11  FPARC    18744 non-null  float64
 12  FSCHP    21395 non-null  int64  
 13  FTAXP    21395 non-null  float64
 14  GASP     21395 non-null  float64
 15  HHL      21395 non-null  float64
 16  HHT      21395 non-null  float64
 17  HINCP    21395 non-null  float64
 18  LANX     20330 non-null  float64
 19  MAR      21395 non-null  int64  
 20  MV       21395 non-null  float64
 21  NRC      21395 non-null  float64
 22  R18      21395 non-null  float64
 23  R65      21395 non-null  float64
 24  RAC1P    21395 non-null  int64  
 25  RMSP     21395 non-null  float64
 26  RWAT     21395 non-null  float64
 27  SCH      20760 non-null  float64
 28  SCHL     20760 non-null  float64
 29  SEX      21395 non-null  int64  
 30  VALP     21395 non-null  float64
 31  VALP_B1  21395 non-null  float64
dtypes: float64(26), int64(6)
memory usage: 5.2 MB
None
'''



class OklahomaService:
    def __init__(self):
        self.oklahoma = pd.read_csv('data/comb32.csv')
        self.my_oklahoma = None
        self.data1 = None
        self.target1 = None
        self.rf1 = None
        self.X_train1 = None
        self.X_test1= None
        self.y_train1= None
        self.y_test1= None
        self.model = None
    '''
    1.스펙보기
    '''
    def spec(self):
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(self.oklahoma.shape)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)
        print(" --- 3.Info ---")
        print(self.oklahoma.info())
        print(" --- 4.Case Top1 ---")
        print(self.oklahoma.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.oklahoma.tail(3))
        print(" --- 6.Describe ---")
        print(self.oklahoma.describe())
        print(" --- 7.Describe All ---")
        print(self.oklahoma.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        t = self.oklahoma
        t.drop('CONP',axis = 1, inplace = True)
        print(t.shape)


        self.my_oklahoma = t.rename(columns=oklahoma_meta)
        print(" --- 2.Features ---")
        print(self.my_oklahoma.columns)

    '''
    3.타깃변수(=종속변수 dependent, Y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: VALP(연속형), VALP_B1(이진값) 주택가격이 중위수 이상이면 1, 아니면 0
    타깃변수값: 
    인터벌 (구간변수)= ['나이','침실수','월 전기료','월 가스비','가계 소득','자녀 수','방 수','주택 가격']
    '''
    def interval_variables(self):
        self.rename_meta()
        pd.options.display.float_format = '{:.2f}'.format
        t = self.my_oklahoma
        interval = ['나이','침실 수','월 전기료','월 가스비','가계 소득','자녀 수','방 수','주택 가격']
        c1 = t['월 전기료'] < 500
        c2 = t['월 가스비'] <= 311
        c3 = t['가계 소득'] <= 320000
        t1 = t[c1 & c2 & c3]
        print(f'이상 값 제거 후 shape : {t1.shape}')
        print(t[interval].skew())
        print(t1[interval].skew())
        print('#######################')
        print(t[interval].kurtosis())
        print(t1[interval].kurtosis())
        print(t1['VALP_B1'].value_counts(normalize=True))
        t1.to_csv("./save/comb31-IQR30.csv",index=False)

    def norminal_variables(self):
        self.interval_variables()
        df = pd.read_csv('./save/comb31-IQR30.csv')
        normina = ['COW','FPARC','LANX','SCH','SCHL']
        print(df[normina].isnull().mean())
        df[normina] = df[normina].fillna(0).astype(np.int64)
        print(df[normina].isnull().mean())
        print(df.shape)
        df_with_VALP_B1 = df.drop(['주택 가격'],axis =1)
        print(df_with_VALP_B1.shape)
        df_with_VALP_B1.to_csv("./save/2017DC1.csv",index=False)
    '''
    4.범주형 = ['COW','FPARC','LANX','SCH','SCHL']
    '''

    def ratio_variables(self): # 해당 컬럼이 없음
        pass


    def ordinal_variables(self): # 해당 컬럼이 없음
        pass

    def target(self):

        df = pd.read_csv('./save/2017DC1.csv')
        print(df.shape)
        data = df.drop(['VALP_B1'],axis=1)
        target = df['VALP_B1']
        self.data1 = data
        self.target1= target
        print(self.data1.shape)
        print(self.target1.shape)

    def partition(self):
        self.target()
        X_train, X_test, y_train, y_test = train_test_split(self.data1, self.target1,
                                                            test_size=0.5, random_state=42, stratify=self.target1)

        self.X_train1, self.X_test1, self.y_train1, self.y_test1 = X_train, X_test, y_train, y_test

    def modeling(self):

        rf = RandomForestClassifier(n_estimators=100,random_state=0)
        self.rf1 = rf


    def learning(self):
        self.partition()
        self.modeling()
        self.model = self.rf1.fit(self.X_train1, self.y_train1)


    def predict(self):
        self.partition()
        self.modeling()
        self.learning()
        pred = self.model.predict(self.X_test1)
        print('트레이닝 셋 정확도 : {:.5f}'.format(self.model.score(self.X_train1,self.y_train1)))
        print('테스트 셋 정확도 : {:.5f}'.format(accuracy_score(self.y_test1,pred)))


