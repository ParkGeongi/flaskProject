from dataclasses import dataclass

@dataclass
class OOP:
    x = 15

    def foo(self):
        x = self.x
        print("OOP 출력: "+str(x))
x = 10
def foo():
    global x
    x = x + 20
    print("FP 출력: "+str(x))

def A_1():
    x=10
    def B():
        x=20
    B()
    print(x)

def A_2():
    x=10
    def B():
        nonlocal x
        x=20
    B()
    print(x)


def A_3():
    x=10
    y=100
    def B():
        x=20
        def C():
            nonlocal x
            nonlocal y
            x = x+30
            y = y+300
            print(x)
            print(y)
        C()
    B()
def calc():
    a = 3
    b = 5
    t = 0
    def mul_add(x):
        nonlocal t
        t = t + a * x + b
        print('클로저 1 결과 : '+ str(t))

    def mul_add_2(x):
        nonlocal t
        t = t + a * x - b
        print('클로저 1 결과 : '+str(t))

    return {'덧셈': mul_add,'뺄셈' : mul_add_2}

MENUS = ['종료', '483.Q1', '483.Q2', '484.Q3','486.Q4']

def menus(menu):
    for i, j in enumerate(menu):
        print(f"{i}. {j}")
    return int(input("메뉴 : "))


if __name__ == '__main__':
    while True:
        menu = menus(MENUS)
        if menu == 0:
            break

        elif menu == 1:
            A_1()

        elif menu == 2:
            A_2()

        elif menu == 3:
            A_3()
        elif menu == 4:
            c= calc()
            print('클로저1 : ' + str(c['덧셈'](2))) # 11
            print('클로저2 : ' + str(c['뺄셈'](2))) # 1
        else:
            print('다시입력')

