# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    num = str(num)
    sum = 0
    for i in num:
        sum += int(i)
    remainder = 3 - sum % 3
    for i in range(len(num)):
        if int(num[i]) + remainder <= 9:
            digit = int(num[i]) + remainder
            while digit + 3 <= 9:
                digit += 3
            new_num = int(num[:i] + str(digit) + num[i + 1:])
            return new_num
        else:
            digit = int(num[-1])
            if remainder == 1:
                digit -= 2
            elif remainder == 2:
                digit -= 1
            else:
                digit -= 3
            new_num = num[:-1] + str(digit)
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')