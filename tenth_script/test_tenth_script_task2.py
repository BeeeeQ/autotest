# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_division_by_integer():
    all_division(5)


def test_division_by_float():
    all_division(4.23)


def test_division_by_zero():
    all_division(0)


@pytest.mark.acceptance
def test_division_by_1():
    all_division(1)


@pytest.mark.acceptance
def test_division_by_billion():
    all_division(1000000000)
