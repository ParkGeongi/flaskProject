'''from machine.stroke import STROKE_MENUS, stroke_menu
from machine.stroke import StrokeService
def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            stroke_menu[menu](t)

            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")

            '''
from machine.oklahoma import OKLAHOMA_MENUS, oklahoma_menu
from machine.oklahoma import OklahomaService


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')


if __name__ == '__main__':
    t = OklahomaService()
    while True:
        menu = my_menu(OKLAHOMA_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            oklahoma_menu[menu](t)

            try:
                oklahoma_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")