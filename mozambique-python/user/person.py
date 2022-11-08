"""
이름 주민번호(950101 - 1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25 (만)
성별: 남성
주소: 서울

검색할 첫글자 입력하면 나오게
*******************************
"""


class Person(object):

    def __init__(self, name, birth, home) -> None:
        self.name = name
        self.birth = birth
        self.home = home
        self.age = 0
        self.gender = ""
    def __str__(self):
        self.get_age()
        self.get_gender()
        return f'{self.name} {self.age} {self.gender} {self.home}'

    def get_age(self):
        birth = self.birth
        if birth[7] == "1":  # gender check 주민 번호 (birth) 7번 째 자리 성별판별번호 인덱스
            self.age = 2022 - 1900 - int(birth[0:2])
        elif birth[7] == "3":
            self.age = 2022 - 2000 - int(birth[0:2])
        elif birth[7] == "2":
            self.age = 2022 - 1900 - int(birth[0:2])
        elif birth[7] == "4":
            self.age = 2022 - 2000 - int(birth[0:2])



    def get_gender(self):
        birth = self.birth
        if birth[7] == "1":
            self.gender = "남"
        elif birth[7] == "3":
            self.gender = "남"
        elif birth[7] == "2":
            self.gender = "여"
        elif birth[7] == "4":
            self.gender = "여"

    @staticmethod
    def delete_person(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]


    @staticmethod
    def new_person():
        return Person(input("이름 : "), input("생년월일 : "), input("주소 : "))

    @staticmethod
    def print_menu():
        print("*" * 30)
        print("1. 개인정보 입력")
        print("2. 개인정보 출력")
        print("3. 개인정보 삭제")
        print("4. 종료")
        menu = int(input("몇번? "))
        return menu
    @staticmethod
    def result(ls):
        print("### 개인정보 등록 ###")
        print("*" * 40)
        print("이름 나이 성별 주소")
        [print(i) for i in ls]
        print("*" * 40)
