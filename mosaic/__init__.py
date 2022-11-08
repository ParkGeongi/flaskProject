
from mosaic.views import MenuController
from util.common import Common
from util.dataset import Dataset
from const.path import HAAR,CTX
'''
이미지 읽기의 flag는 3가지가 있습니다.
cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 
                    투명한 부분은 무시되며, Default값입니다.
cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 
                        실제 이미지 처리시 중간단계로 많이 사용합니다.
cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다
3개의 flag대신에 1, 0, -1을 사용해도 됩니다
Shape is (512, 512, 3)
Y축: 512 (앞)
X축: 512 (뒤)
3은 RGB 로 되어 있다.
cv2.waitKey(0) : keyboard입력을 대기하는 함수로 
                0이면 key입력까지 무한대기이며, 특정 시간동안 대기하려면 
                milisecond값을 넣어주면 됩니다.
cv2.destroyAllWindows() 화면에 나타난 윈도우를 종료합니다. 
                        일반적으로 위 3개는 같이 사용됩니다.
'''
ds = Dataset()
api = MenuController()
URL = "https://docs.opencv.org/4.x/roi.jpg"
IMG = "Lenna.png"
BUILDING ='https://www.charlezz.com/wordpress/wp-content/uploads/2021/06/www.charlezz.com-opencv-building.jpg'
HAAR = CTX + HAAR
GIRL = "girl.jpg"
GIRL_INCLINED = "girl_inclined.png"
GIRL_WITH_MOM = "girl_with_mom.jpg"
PEOPLE= "1.jpg"
GIRL_SIDE_FACE = "girl_side_face.jpg"
FACE_TARGET = ""
FACE_OBJECT = ""
CAT = "cat.jpg"

if __name__ == '__main__':
    menus = ["종료", "원본보기", "그레이 스케일","엣지 검출 disk","엣지 검출 memory","직선 검출","얼굴 인식","고양이 모자이크","소녀 모자이크", "모녀 모자이크","전체보기"]

    while True:

        menu = Common.menu(menus)
        if menu == "0":
            print(f" ### {menus[0]} ### ")
            break
        elif menu == "1": api.Menu_1_Origin(menus[1],URL)
        elif menu == "2": api.Menu_2_Gray(menus[2],URL)
        elif menu == "3": api.Menu_3_CannyDisk(menus[3],IMG)
        elif menu == '4': api.Menu_4_CannyMemory(menus[4],URL)
        elif menu == '5': api.Menu_5_Hough(menus[5],BUILDING)
        elif menu == '6': api.Menu_6_Haar(menus[6],HAAR,PEOPLE)
        elif menu == '7': api.Menu_7_Mosaic_Cat(menus[7], CAT)
        elif menu == '8': api.Menu_8_Mosaic_Girl(menus[8],HAAR, GIRL)
        elif menu == '9': api.Menu_9_Mosaic_Two(menus[9], HAAR, PEOPLE)
        elif menu == '10':api.Menu_10_All_View(menus[10], HAAR, GIRL, GIRL_WITH_MOM)

        else:
            print(" ### 해당 메뉴 없음 ### ")


