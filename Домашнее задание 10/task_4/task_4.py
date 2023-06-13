# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('print_start_end')
class TestClass():

    def test_smoke_division_positive_numbers(self, print_time):
        result = all_division(10, 2)
        assert result == 5

    def test_division_negative_numbers(self):
        result = all_division(-10, -2)
        assert result == 5


