import pytest
import datetime

@pytest.fixture(scope='class')
def print_start_end():
    start = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Начало выполнения в {start}\n')
    yield
    end = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Завершение работы в {end}\n')


@pytest.fixture(scope='function')
def print_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Тест прошел за {(end - start)}')