import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from const.path import CTX


class Midwest(object):
    def __init__(self, mid):
        self.mid = mid

    def print_meta(self):
        print(self.mid.columns)

    def rename(self):
        self.mid.rename(columns = {'poptotal' : 'total'},inplace=True)
        self.mid.rename(columns = {'popasian' : 'asian'},inplace=True)
        print(self.mid.columns)

    def drived_variable(self):

        self.mid['백분율'] = ((self.mid['asian']) / (self.mid['total'])) * 100
        print(self.mid)
    def judge(self):

        self.mid['test'] = np.where(self.mid['백분율'] >= self.mid['백분율'].mean(), 'large', 'small')
        print(self.mid)
    def graph(self):

        count_test = self.mid['test'].value_counts()
        count_test.plot.bar(rot = 0)
        plt.savefig('mid_graph.png')
        plt.show()


def load(file):
    mid = pd.read_csv(file)
    return mid

def menu_st(menus):
    for i, j in enumerate(menus):
        print(f"{i}. {j}")
    return int(input('메뉴 선택 '))

MENUS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]
CSV = 'midwest.csv'



if __name__ == '__main__':
    mw = load(CTX + CSV)
    t = Midwest(mw)
    while True :
        menu = menu_st(MENUS)


        if menu == 0:
            break
        elif menu == 1:
            t.print_meta()
        elif menu == 2:
            t.rename()
        elif menu == 3:
            t.rename()
            t.drived_variable()
        elif menu == 4:
            t.rename()
            t.drived_variable()
            t.judge()
        elif menu == 5:
            t.rename()
            t.drived_variable()
            t.judge()
            t.graph()
