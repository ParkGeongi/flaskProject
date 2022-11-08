import pandas as pd


def new_fruits_df():

    #ls = [['제품','사과'],['가격',1800],['제품','딸기'],['가격',1500]]
    ls = ['제품','가격','판매량','']
    ls1 = [['사과','딸기','수박'],[1800,1500,3000],[24,38,13],['','','']]
    df = pd.DataFrame({j : ls1[i]for i , j in enumerate(ls)})
    df = df.set_index("")
    print(df)

    print(int(sum(df['가격']) / 3))
    print(int(sum(df['판매량']) / 3))
if __name__ == '__main__':
    new_fruits_df()

