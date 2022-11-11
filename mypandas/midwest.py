import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, font_manager, rc

warnings.simplefilter(action='ignore', category=FutureWarning)
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family =font)
d
my_meta = {
    'PID' : "신원확인",
    'county' : '군',
    'state' : "주",
    "area" : '지역',
    'poptotal' : '전체 인구 수',
    'popdensity' : '인구 밀도',
    'popwhite' : '백인 인구 수',
    'popblack' : '흑인 인구 수',
    'popamerindian' : '미국 인구 수',
    'popasian': '아시아 인구 수',
    'popother': '그 외 인구수',
    'percwhite': '백인 비율',
    'percblack': '흑인 비율',
    'percamerindan': '미국인 비율',
    'percasian': '아시아인 비율',
    'percother': '그 외 비율',
    'popadults': '성인 인구 수',
    'perchsd':'high school density?(hsd) 비율',
    'percollege':'대학생 비율',
    'percprof':'교수 비율',
    'poppovertyknown': '알려진 빈곤 인구 수',
    'percpovertyknown':'알려진 빈곤 비율',
    'percbelowpoverty':'완전 빈곤(정부 지원 필요) 비율',
    'percchildbelowpovert':'완전 빈곤(정부 지원 필요) 어린이 비율',
    'percadultpoverty':'어른 빈곤 비율',
    'percelderlypoverty':'빈곤 노인 비율',
    'inmetro':'지하철 구역',
    'category':'카테고리'
}

'''
Index(['PID', 'county', 'state', 'area', 'poptotal', 'popdensity', 'popwhite',
       'popblack', 'popamerindian', 'popasian', 'popother', 'percwhite',
       'percblack', 'percamerindan', 'percasian', 'percother', 'popadults',
       'perchsd', 'percollege', 'percprof', 'poppovertyknown',
       'percpovertyknown', 'percbelowpoverty', 'percchildbelowpovert',
       'percadultpoverty', 'percelderlypoverty', 'inmetro', 'category'],
      dtype='object')
'''

class Midwest(object):

    def __init__(self):
        self.mid = pd.read_csv('./data/midwest.csv')
        self.my_mid = None

    def print_meta(self):
        print(self.mid.columns)

    def rename(self):
        self.my_mid = self.mid.rename(columns = my_meta)
        print(self.my_mid.columns)

    def drived_variable(self):
        self.rename()
        test = self.my_mid
        test['백분율'] = ((test['아시아 인구 수']) / (test['전체 인구 수'])) * 100
        self.my_mid = test
        print(self.my_mid)

    def judge(self):
        self.drived_variable()
        self.my_mid['테스트'] = np.where(self.my_mid['백분율'] >= self.my_mid['백분율'].mean(), 'large', 'small')

        print(self.my_mid)
        self.my_mid.plot.hist()
        plt.show()
    def graph(self):
        self.judge()

        count_test = self.my_mid['테스트'].value_counts()
        print(count_test)
        count_test.plot.bar(rot = 0)
        plt.savefig('./save/mid_graph.png')
        plt.show()



def menu_st(menus):
    for i, j in enumerate(menus):
        print(f"{i}. {j}")
    return int(input('메뉴 선택 '))

MENUS = ["종료",
         "메타데이터 출력",
         "메타데이터를 한글로 변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]

if __name__ == '__main__':

    t = Midwest()

    while True :
        menu = menu_st(MENUS)

        if menu == 0:
            break
        elif menu == 1:
            t.print_meta()

        elif menu == 2:
            t.rename()

        elif menu == 3:
            t.drived_variable()

        elif menu == 4:
            t.judge()

        elif menu == 5:
            t.graph()
