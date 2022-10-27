from user.bmi import Bmi
from util.common import Common
from user.contacts import Contact
from user.grade import Grade
from user.person import Person


ls1 = []
ls2 = []
ls_3 = []
ls4 = []
while True:
    menu = Common.menu(["종료","BMI","주소록","성적표","개인정보"])
    if menu == "0":
        print("### 앱 종료 ###")
        break
    elif menu == "1":
        print("### BMI ###")
        submenu = Common.menu(["종료", "BMI등록", "BMI목록", "BMI삭제"])
        if submenu == "0": break
        elif submenu == "1":
            biman = Bmi.new_bmi()
            ls1.append(biman)
        elif submenu == 2:
            Bmi.result(ls1)
        elif submenu == 3:
            Bmi.delete_bmi(ls1, input("삭제할 이름 : "))
    elif menu == 2:
        print("### 주소록 ###")
        submenu_2 = Common.menu(["종료", "Contact 등록", "Contact 목록", "Contact 삭제"])
        if submenu_2 == 0: break
        elif submenu_2 == 1:
            contact = Contact.new_contact()
            ls2.append(contact)
        elif submenu_2 == 2:
            Contact.result(ls2)
        elif submenu_2 == 3:
            Contact.delete_contact(ls2,input("삭제할 이름 : "))

    elif menu == 3:
        print("### 성적표 ###")
        submenu_3 = Common.menu(["종료", "Grade 등록", "Grade 목록", "Grade 삭제"])
        if submenu_3 ==0:
            break
        elif submenu_3 == 1:
            grade = Grade.new_grade()
            ls_3.append(grade)
        elif submenu_3 == 2:
            Grade.result(ls_3)
        elif submenu_3 == 3:
            Grade.delete_grade(ls_3,input("삭제할 이름 : "))


    elif menu == 4 :
        print("### 개인정보 ###")
        submenu_4 = Common.menu(["종료", "개인정보 등록", "개인정보 목록", "개인정보 삭제"])
        if submenu_4 == 0: break

        elif submenu_4 == 1:
            person = Person.new_person()
            ls4.append(person)
        elif submenu_4 == 2:
            Person.result(ls4)
        elif submenu_4 == 3:
            Person.delete_person(ls4, input("삭제할 이름 : "))

    else:
        print("잘못된 메뉴 번호 입니다.")