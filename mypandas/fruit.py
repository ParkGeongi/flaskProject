import numpy as np
import pandas as pd
from string import ascii_lowercase

def new_fruits_df():
    #ls = [['제품','사과'],['가격',1800],['제품','딸기'],['가격',1500]]
    ls = ['제품','가격','판매량','']
    ls1 = [['사과','딸기','수박'],[1800,1500,3000],[24,38,13],['','','']]
    df = pd.DataFrame({j : ls1[i]for i , j in enumerate(ls)})
    df = df.set_index("")
    print(df)
    print('*'*30)
    a =  int(df['가격'].mean())
    b = int(df['판매량'].mean())
    print(f'가격 평균 : {a}')
    print(f'판매량 평균 : {b}')
    print('*' * 30)

def new_number_2d():

    ls = list(range(1,31)) #타입 변환
    df = pd.DataFrame(np.array([ls[0:10],
                                ls[10:20],
                                ls[20:30]]),
                      columns = list(ascii_lowercase[0:10]))

    print('*' * 50)
    print(df.head())
    print('*' * 50)

def my_list(a,b):

    return list(range(a,b))

def menu_st(a):
    [print(f' ### {i}. {j} ### ') for i,j in enumerate(a)]
    return int(input('메뉴 입력 : '))

MENUS = ['종료','2D 과일','2D 숫자']

if __name__ == '__main__':

    while True:
        menu = menu_st(MENUS)
        if menu == 0:
            break
        elif menu == 1:
            new_fruits_df()
        elif menu == 2:
            new_number_2d()

###############