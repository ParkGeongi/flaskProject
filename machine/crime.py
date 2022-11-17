import googlemaps
import numpy as np
import pandas as pd
from branca.colormap import linear
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import folium
import json
CRIME_MENUS = ["종료", #0
                "SPEC",#1
                'Save Police Position',#2
                "Save CCTV Population",#3 여러개 객체를 merge
                "Save Police Normalization",#4
                "folium",#5
                "Partition",#6
                "모델링",#7
                "학습",#8
                "예측"]#9


crime_menu = {

    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pos(),
    "4" : lambda t: t.save_cctv_norm(),
    "5" : lambda t: t.folium_ex()




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
        cols = ['절도 발생','절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)  # regex=True
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.ls = [self.crime,self.cctv]
        self.my_crime = None
        self.my_cctv = None
        self.pop = pd.read_excel("./data/pop_in_seoul.xls", header = 0,skiprows = [0,2],usecols = 'B, D, G, J, N')#header 보다 skiprow먼저 실행되고  header실행됨
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
        self.us_states = './data/us-states.json'
        self.us_unemployment = pd.read_csv('./data/us_unemployment.csv')




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
        crime.to_pickle('./pickle/police_pos.pkl')

        #crime.to_csv('./pickle/police_pos.csv', index=False)

    def save_cctv_pos(self):
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'},inplace=True)
        pop.rename(columns = {
            pop.columns[0] : '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
        },inplace=True)

        pop.drop([26], inplace= True)

        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100 # ratio
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100 # ratio

        cctv.drop(['2013년도 이전','2014년','2015년','2016년'],axis = 1,inplace=True)
        cctv_pop = pd.merge(cctv,pop, on = '구별')

        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """
        cctv_pop.to_pickle('./pickle/cctv_pop.pkl')
        print(pd.read_pickle('./pickle/cctv_pop.pkl'))

        print()
    def save_cctv_norm(self):
        police_pos = pd.read_pickle('./pickle/police_pos.pkl')
        print(police_pos)
        police = pd.pivot_table(police_pos, index='구별',aggfunc=np.sum)
        print(police)
        police['살인검거율'] = (police['살인 검거'].astype(int)/police['살인 발생'].astype(int))*100
        police['강도검거율'] = (police['강도 검거'].astype(int) / police['강도 발생'].astype(int)) * 100
        police['강간검거율'] = (police['강간 검거'].astype(int) / police['강간 발생'].astype(int)) * 100
        police['절도검거율'] = (police['절도 검거'].astype(int) / police['절도 발생'].astype(int)) * 100
        police['폭력검거율'] = (police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int)) * 100
        police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1, inplace=True)
        for i in self.crime_rate_columns:
            police.loc[police[i] > 100,1] = 100  # 데이터값의 기간 오류로 100을 넘으면 100으로 계산
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns].values
        min_max_scalar = preprocessing.MinMaxScaler()
        """
          스케일링은 선형변환을 적용하여
          전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
          """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        """
         정규화 normalization
         많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
         분포(스케일)를 유사하게 만드는 작업
         """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns,index=police.index)

        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis = 1)
        police_norm['검거'] = np.sum(police_norm[self.crime_rate_columns], axis = 1)
        police_norm.to_pickle('./pickle/police_norm.pkl')
        print(pd.read_pickle('./pickle/police_norm.pkl'))

    def folium_ex(self):

        #us_states = self.us_states
        us_unemployment = self.us_unemployment
        bins = list(us_unemployment['Unemployment'].quantile([0, 0.25, 0.5, 0.75, 1]))
        m = folium.Map(location=[48,-102], zoom_start=5)

        url = (
            "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
        )
        state_geo = f"{url}/us-states.json"
        state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
        state_data = pd.read_csv(state_unemployment)

        folium.Choropleth(
            geo_data=state_geo,
            data=state_data,
            name='choropleth',
            columns=['State','Unemployment'],
            key_on='feature.id',
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='Unemployment_rate(%)',
            bins=bins,
            reset=True

        ).add_to(m)

        folium.LayerControl().add_to(m)

        m.save('./save/unemployment.html')


    def norminal(self):
        pass
    def ratio(self):
        pass
