from const.path import CTX
from mypandas.mpg import Test,menu_st,load

CSV = 'mpg.csv'
mpg = load(CTX +CSV)
menus = ['종료','head','tail','shape','info','describe','rename','merge & where','graph']
#cty와 hwy merge하여 total 변수 생성
'''
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64  
 1   manufacturer  234 non-null    object 
 2   model         234 non-null    object 
 3   displ         234 non-null    float64
 4   year          234 non-null    int64  
 5   cyl           234 non-null    int64  
 6   trans         234 non-null    object 
 7   drv           234 non-null    object 
 8   cty           234 non-null    int64  
 9   hwy           234 non-null    int64  
 10  fl            234 non-null    object 
 11  class         234 non-null    object 
dtypes: float64(1), int64(5), object(6)
'''
if __name__ == '__main__':
    while True :
        menu = menu_st(menus)
        t = Test(mpg)
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
            t.describe()
        elif menu == 6:
            t.rename()
        elif menu == 7:
            t.derived_variable()
        elif menu == 8:
            t.graph_test()