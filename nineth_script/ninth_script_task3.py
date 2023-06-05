# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
count = 0
sums_list = []
temp = 0
with open('test_file/task_3.txt', 'r') as file:
    for index, line in enumerate(file.readlines()):
        if not line == '\n':
            temp += int(line)
        else:
            sums_list.append(temp)
            temp = 0

three_most_expensive_purchases = sum(sorted(sums_list)[-3:])

assert three_most_expensive_purchases == 202346
