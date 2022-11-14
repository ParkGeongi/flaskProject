from ml.views import StrokeController
from titanic.template import Plot

from util.common import Common

fname = 'healthcare-dataset-stroke-data.csv'
if __name__ == '__main__':

    while True:
        api = StrokeController()
        menu = Common.menu(["종료","문제제기","데이터구하기",
                            "타겟변수설정",'데이터처리','시각화','모델링'
                            ,'학습','예측']) #모델링 : 전처리 + 모델 + 후처리 여러번 함

        if menu == "0": break

        elif menu == "1":
            print(" ### 문제제기 ###")


        elif menu == "2":
            print(" ### 데이터구하기 ###")
            api.set_data(fname)


        elif menu == "3":
            print(" ### 타겟변수 설정 ###")
            api.create_target(fname)


        elif menu == "4":
            print(" ### 데이터처리 ###")
            api.data_processing(fname)


        elif menu == "5":
            print(" ### 시각화 ###")


        elif menu == "6":
            print(" ### 모델링 ###")


        elif menu == "7":
            print(" ### 학습 ###")

        elif menu == "8":
            print(" ### 예측 ###")

        else:
            print(" 해당 메뉴 없음 ")


