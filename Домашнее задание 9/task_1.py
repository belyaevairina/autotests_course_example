# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

def cleaning_text():
    data_file = Path("test_file/task1_data.txt")
    answer_file = Path("test_file/task1_answer.txt")

    with open(data_file, mode='r', encoding='utf-8') as data_file:
        data = data_file.readlines()

    with open(answer_file, mode='w', encoding='utf-8') as answer_file:
        for row in data:
            new_row = ''
            for letter in row:
                if not letter.isdigit():
                    new_row += letter
            answer_file.write(new_row)

cleaning_text()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')