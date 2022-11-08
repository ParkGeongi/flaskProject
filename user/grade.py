class Grade(object):
    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = 0
        self.avg = 0
        self.grade = ""
    def __str__(self):
        return f"{self.name} {self.ko} {self.en} {self.ma} {self.get_total()} {round(self.get_avg(),2)} {self.get_grade()}"
    def get_total(self):
        self.total = self.ko + self.en + self.ma
        return self.total

    def get_avg(self):
        total = self.get_total()
        self.avg = total / 3
        return self.avg

    def get_grade(self):
        avg = self.avg
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else:
            grade = "F"
        self.grade = grade
        return grade

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]


    @staticmethod
    def new_grade():
        return Grade(input("이름 : "), int(input("국어 : ")), int(input("영어 : ")), int(input("수학 : ")))

    @staticmethod
    def print_menu():
        print("*" * 30)
        print("1. 성적 입력")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료")
        menu = int(input("몇번? "))
        return menu

    @staticmethod
    def result(ls):
        print("### 성적표 등록 ###")
        print("*" * 40)
        print("이름 국어 영어 수학 총점 평균 등급")
        [print(i) for i in ls]
        print("*" * 40)