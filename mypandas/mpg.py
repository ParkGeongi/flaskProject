import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

my_meta = {
    "manufacturer": "회사",
    "model": "모델",
    "displ": "배기량",
    "year": "연식",
    "cyl": "실린더",
    "trans": "차축",
    "drv": "오토",
    "cty": "시내연비",
    "hwy": "시외연비",
    "fl": "연료",
    "class": "차종"
}

'''
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64  
 1   manufacturer  234 non-null    object 회사
 2   model         234 non-null    object 모델
 3   displ         234 non-null    float64 배기량
 4   year          234 non-null    int64  연식
 5   cyl           234 non-null    int64  실린더
 6   trans         234 non-null    object 차축
 7   drv           234 non-null    object 오토
 8   cty           234 non-null    int64  시내연비
 9   hwy           234 non-null    int64 시외연비
 10  fl            234 non-null    object 연료
 11  class         234 non-null    object 차종
dtypes: float64(1), int64(5), object(6)
'''

def menu_st(menus):
    for i, j in enumerate(menus):  # ["종료", "등록", "출력", "삭제"]
        print(f"{i}. {j}")
    return int(input('메뉴 선택 '))

class Test(object):
    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')
        self.my_mpg = None

    def head(self):
        print(self.mpg.head())

    def tail(self):
        print(self.mpg.tail())

    def shape(self):
        print(self.mpg.shape)

    def info(self):
        print(self.mpg.info())

    def descride(self):
        print(self.mpg.describe())

    def describe_all(self):
        print(self.mpg.describe(include='all'))

    def change_meta(self):
        self.my_mpg = self.mpg.rename(columns=my_meta)

    def derived_variable(self):
        self.change_meta()
        t = self.my_mpg
        t['총연비'] = (t['시내연비'] + t['시외연비'])/2
        t['연비테스트'] = np.where(t['총연비']>=20, 'pass', 'fail')
        self.my_mpg = t
        print(self.my_mpg.columns)
        print(self.my_mpg.head())

    def graph_test(self):

        self.derived_variable()
        count_test =self.my_mpg['연비테스트'].value_counts()
        count_test.plot.bar(rot = 0)
        plt.show()
        print(count_test)

    def graph_save(self):
        self.graph_test()
        count_test = self.my_mpg['연비테스트'].value_counts()
        count_test.plot.bar(rot=0)
        plt.savefig('mpg.png')

    def displ(self):
        self.change_meta()
        t = self.my_mpg
        displ1 = t.query('배기량<= 4')[['시외연비']]
        displ2 = t.query('배기량>= 5')[['시외연비']]
        mean1 =displ1['시외연비'].mean()
        mean2 = displ2['시외연비'].mean()
        print(f'배기량 4 이하 도시 연비 : {mean1}')
        print(f'아우디 5 이상 도시 연비 : {mean2}')
    def comp_cty(self):
        self.change_meta()
        t = self.my_mpg

        cty1 = t.query('회사.str.contains("audi")')
        cty2 = t.query('회사.str.contains("toyota")')

        mean1 = cty1['시내연비'].mean()
        mean2 = cty2['시내연비'].mean()

        print(f'아우디 연비 : {mean1}')
        print(f'도요타 연비 : {mean2}')

    def comp_three(self):
        self.change_meta()
        t = self.my_mpg

        hwy1 = t.query('회사.str.contains("chevrolet")')
        hwy2 = t.query('회사.str.contains("ford")')
        hwy3 = t.query('회사.str.contains("honda")')

        print(f'chevrolet : {hwy1}')
        print(f'ford : {hwy2}')
        print(f'honda : {hwy3}')

        sum = hwy1['시외연비'].sum() +hwy2['시외연비'].sum() +hwy3['시외연비'].sum()
        count = hwy1['시외연비'].count() + hwy1['시외연비'].count() + hwy1['시외연비'].count()

        print(f'시외연비 전체 평균 : {sum / count}')

    def cty_two(self):

        self.change_meta()
        t = self.my_mpg

        cty1 = t.query('차종.str.contains("suv")')
        cty2 = t.query('차종.str.contains("compact")')
        mean1 = cty1['시내연비'].mean()
        mean2 = cty2['시내연비'].mean()
        print(f'suv 시내연비 평균 : {mean1}')
        print(f'compact 시내연비 평균 : {mean2}')

    def audi_comp(self):
        self.change_meta()
        t = self.my_mpg

        audi = t.query('회사.str.contains("audi")')
        audi_sort = audi.sort_values('시외연비',ascending= False)
        print(audi_sort.head(5))

    def eff_rank(self):
        self.change_meta()
        t = self.my_mpg
        t['total_eff'] = t['시내연비'] +t['시외연비']
        t['mean_eff'] = t['total_eff'] / 2
        sort_eff = t.sort_values('mean_eff',ascending= False)
        print(sort_eff.head(3))


menus = ['종료','head','tail','shape','info','descride','describe all','rename','merge & where','graph',
         'graph save',
         "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
         "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
         "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
         'suv/ 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 높은가?', # mpg 150페이지 문제
         '아우디차에서 고속도로 연비 1~5위 출력하시오',  # mpg 153페이지 문제
         '평균연비가 가장 높은 자동차 1~3위 출력하시오'# mpg 158페이지 문제
         ]

#cty와 hwy merge 하여 total 변수 생성

t = Test()

if __name__ == '__main__':
    while True :
        menu = menu_st(menus)

        if menu == 0:
            break
        elif menu == 1:
            t.head()
        elif menu == 2:
            t.tail()
        elif menu == 3:
            t.shape()
        elif menu == 4:
            t.info()
        elif menu == 5:
            t.descride()
        elif menu == 6:
            t.describe_all()
        elif menu == 7:
            t.change_meta()
        elif menu == 8:
            t.derived_variable()
        elif menu == 9:
            t.graph_test()
        elif menu == 10:
            t.graph_save()
        elif menu == 11:
            t.displ()
        elif menu == 12:
            t.comp_cty()
        elif menu == 13:
            t.comp_three()
        elif menu == 14:
            t.cty_two()
        elif menu == 15:
            t.audi_comp()
        elif menu == 16:
            t.eff_rank()