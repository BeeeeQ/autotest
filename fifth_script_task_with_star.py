# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
Метод принимает число (год) и возвращает строку с годом в виде римской записи
    :param val: Год цифрами
    :return: Год римской записью
    """
    # Здесь нужно написать код
    dict_roman = {1: 'I',
                  5: 'V', 10: 'X',
                  50: 'L', 100: 'C',
                  500: 'D', 1000: 'M'}
    thousands, hundred, tens, ones = val // 1000, val // 100 % 10, val // 10 % 10, val % 10
    thousands = thousands * dict_roman.get(1000)

    def get_roman_str(num: int, factor: int) -> str:
        """
Метод принимает два параметра число и множитель (разрядность - единицы, десятки или сотни)
и возвращает строку римской записью
        :param num: Число
        :param factor: Разрядность числа - единицы, десятки или сотни
        :return:
        """
        if num < 4:
            roman_value = num * dict_roman.get(1 * factor)
        elif num == 4:
            roman_value = dict_roman.get(1 * factor) + dict_roman.get(5 * factor)
        elif 5 <= num < 9:
            roman_value = dict_roman.get(5 * factor) + dict_roman.get(1 * factor) * (num - 5)
        else:
            roman_value = dict_roman.get(1 * factor) + dict_roman.get(10 * factor)
        return roman_value

    hundred = get_roman_str(hundred, 100)
    tens = get_roman_str(tens, 10)
    ones = get_roman_str(ones, 1)
    roman_str = thousands + hundred + tens + ones

    return roman_str


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']

for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
