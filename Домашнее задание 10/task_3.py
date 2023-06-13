# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('number1, number2, result', [
    pytest.param(18, 9, 2, marks=pytest.mark.smoke),
    (-18, 2, -9),
    (-16, -4, 4),
    pytest.param(10, 0, ZeroDivisionError, marks=pytest.mark.skip(reason="Не проверяем деление на 0"))],
    ids=['positive numbers', 'positive and negative numbers', 'negative numbers', 'zero division'])
def test_positive(number1, number2, result):
    assert all_division(number1, number2) == result