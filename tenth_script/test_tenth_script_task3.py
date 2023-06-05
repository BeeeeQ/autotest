# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('num', [
    pytest.param([5, 100, 1000], marks=pytest.mark.smoke),
    pytest.param([5.23, 999.99], marks=pytest.mark.acceptance),
    0,
    pytest.param(1000000000, marks=pytest.mark.skip('unusual'))],
                         ids=['integer', 'float', 'zero', 'billion'])
def test_division(num):
    all_division(num)


