# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path

data_file = Path("test_file/task_3.txt")

with open(data_file, mode='r', encoding='utf-8') as data_file:
    data = data_file.readlines()

buy_list = []
buy = 0
for price in data:
    if price != '\n':
        buy += int(price)
    else:
        buy_list.append(buy)
        buy = 0

buy_list.sort(reverse=True)
three_most_expensive_purchases = sum(buy_list[:3])


assert three_most_expensive_purchases == 202346