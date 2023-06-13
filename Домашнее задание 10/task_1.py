# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    while True:
        letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
        first_word = ''
        second_word = ''
        for i in range(random.randint(1, 15)):
           first_word += random.choice(letters_list)
        for i in range(random.randint(1, 15)):
            second_word += random.choice(letters_list)
        yield f'{first_word} {second_word}'

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))