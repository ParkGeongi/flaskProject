import googlemaps
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
CRIME_MENUS = ["종료", #0
                "데이터 구조",#1
                'Merge',#2  여러개 객체를 merge
                "excel",#3
                "범주형변수편집",#4
                "타겟",#5
                "파티션",#6
                "모델링",#7
                "학습",#8
                "예측"]#9


crime_menu = {

    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3": lambda t: t.excel()


}
'''
CRIME DF
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31 entries, 0 to 30
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   관서명     31 non-null     object
 1   살인 발생   31 non-null     int64 
 2   살인 검거   31 non-null     int64 
 3   강도 발생   31 non-null     int64 
 4   강도 검거   31 non-null     int64 
 5   강간 발생   31 non-null     int64 
 6   강간 검거   31 non-null     int64 
 7   절도 발생   31 non-null     object
 8   절도 검거   31 non-null     object
 9   폭력 발생   31 non-null     object
 10  폭력 검거   31 non-null     object
dtypes: int64(6), object(5)
memory usage: 2.8+ KB
None
'''
'''
CCTV DF
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   기관명        25 non-null     object
 1   소계         25 non-null     int64 
 2   2013년도 이전  25 non-null     int64 
 3   2014년      25 non-null     int64 
 4   2015년      25 non-null     int64 
 5   2016년      25 non-null     int64 
dtypes: int64(5), object(1)
memory usage: 1.3+ KB
None
'''

class CrimeService:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.ls = [self.crime,self.cctv]
        self.my_crime = None
        self.my_cctv = None
        self.pop = pd.read_excel("./data/pop_in_seoul.xls",header = 1 ,skiprows = [2],usecols = 'B, D, G, J, N')


    '''
    1.스펙보기

    3.타깃변수(=종속변수 dependent, Y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: VALP(연속형), VALP_B1(이진값) 주택가격이 중위수 이상이면 1, 아니면 0
    타깃변수값: 
    인터벌 (구간변수)= ['나이','침실수','월 전기료','월 가스비','가계 소득','자녀 수','방 수','주택 가격']
    '''

    def spec(self):
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows', None)

        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                            f"--- 2.Features ---\n{x.columns}\n"
                            f"--- 3.Info ---\n{x.info}\n"
                            f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                            f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                            f"--- 6.Describe ---\n{x.describe()}\n"
                            f"--- 7.Describe All ---\n{x.describe(include='all')}"))(i) for i in self.ls]

    def save_police_pos(self):

        crime = self.crime
        station_names = []

        for name in crime['관서명']:
            print(f'지역이름: {name}')
            station_names.append(f'서울{str(name[:-1])}경찰서')

        print(f'서울시내 경찰서는 총 {len(station_names)}개 이다.')
        [print(i) for i in station_names]
        gmaps = (lambda x : googlemaps.Client(key = x))('')
        print(gmaps.geocode('서울중부경찰서',language = 'ko'))
        station_addrs = []
        station_lats = []
        station_lngs =[]


        for i, name in enumerate(station_names):
            _=gmaps.geocode(name, language = 'ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv', index=False)

    def excel(self):

        print(self.pop)
        #3행제거 2행 metadata -> 1 3 6 9 13


    def interval_variables(self):
        #self.rename_meta()
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
        #self.interval_variables()
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
        #self.target()
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
        #self.partition()
        #self.modeling()
        #self.learning()
        pred = self.model.predict(self.X_test1)
        print('트레이닝 셋 정확도 : {:.5f}'.format(self.model.score(self.X_train1, self.y_train1)))
        print('테스트 셋 정확도 : {:.5f}'.format(accuracy_score(self.y_test1, pred)))


