import os

#  Задание 1

side = 2

# Расчет периметра
perimeter = 4 * side

# Расчет площади
area = side ** 2

# Расчет диагонали
diagonal = (2 * side ** 2) ** 0.5


print("Периметр квадрата:", perimeter)
print("Площадь квадрата:", area)
print("Диагональ квадрата:", diagonal)

#  Задание 2

a = 23  # Коэффициент x^2
b = 33  # Коэффициент x: "))
c = 7  # Постоянный член:"))

# Вычисление дискриминанта
D = (b**2) - (4*a*c)

# Проверка, что дискриминант больше 0
if D > 0:
    # Нахождение корней и округление до 2 знаков после запятой
    root1 = (-b + (D**0.5)) / (2*a)
    root2 = (-b - (D**0.5)) / (2*a)
    print("Корни :", round(root1, 2), "и", round(root2, 2))
else:
    print("Уравнение не имеет действительных корней")

#  Задание 3

string1 = "Hello world"
string2 = "Python is awesome"

# Меняем местами первые два символа у строк
line1 = string2[0:2] + string1[2:]
line2 = string1[0:2] + string2[2:]

print(f'{string1} {string2}', f'{line1} {line2}', sep='\n')

#  Задание 4


# Путь до файла
file_path = "D:/Users/user/pictures/image234.png"

# Имя файла
file_name = os.path.basename(file_path).split('.')[0]

# Диск и корневая папка
drive = os.path.splitdrive(os.path.abspath(file_path))[0][:-1]
root_folder = os.path.splitdrive(file_path)[1].split('/')[1]

# Выводим
print("Имя файла:", file_name)
print("Имя диска:", drive)
print("Корневая папка:", root_folder)

#  Задание 5

a = 10
b = 15

sum_format = "{} + {} = {}".format(a, b, a+b)
multiplication_format = "{} * {} = {}".format(a, b, a*b)

print(sum_format)
print(multiplication_format)

#  Задание 6

string = "Hello world"
new_string = ""

for index, char in enumerate(string):
    if index % 2 == 0:
        new_string += char

print(new_string)

#  Задание 7

# Наши строки
first = 'wtf'
second_str = "brick quz jmpy veldt whangs fox"

# Находим индексы всех символов из строки 1 в строке 2
indices = [second_str.find(list(first)[0]), second_str.find(list(first)[1]), second_str.find(list(first)[2])]

# Находим срез строки от минимального до максимального + 1 индекса
minimum_length_cut = second_str[min(indices):max(indices) + 1]

print(minimum_length_cut)
