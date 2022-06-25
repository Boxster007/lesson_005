# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
import burger
# TODO здесь ваш код
def standard_burger():
    burger.buns()
    burger.cutlets()
    burger.cucumber()
    burger.tomato()
    burger.mayonnaise()
    burger.cheese()
    print("Стандартный бургер готов!")


standard_burger()


def double_cheezeburger():
    burger.buns()
    burger.cutlets()
    burger.cheese()
    burger.cucumber()
    burger.tomato()
    burger.mayonnaise()
    burger.cheese()
    burger.cutlets()
    print("Двойной чизбургер готов!")


double_cheezeburger()