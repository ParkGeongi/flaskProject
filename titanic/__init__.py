
from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common


if __name__ == '__main__':

    while True:
        api = TitanicController()
        menu = Common.menu(["종료","시각화","모델링","머신러닝","베포"]) #모델링 : 전처리 + 모델 + 후처리 여러번 함

        if menu == "0": break

        elif menu == "1":
            print(" ### Visualization ###")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()

        elif menu == "2":
            print(" ### Modeling ###")
            df = api.modeling('train.csv','test.csv')
            print(this.train.head())
            print(this.train.columns)

        elif menu == "3":
            print(" ### Machine Learning ###")
            api.learning('train.csv','test.csv')

        elif menu == "4":
            print(" ### release ###")
            df = api.sumit('train.csv','tset.csv')

        else:
            print(" 해당 메뉴 없음 ")


