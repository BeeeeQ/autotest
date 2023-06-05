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
import string


# Здесь пишем код

def generate_random_name():
    while True:
        word_len1 = random.randint(1, 15)
        word_len2 = random.randint(1, 15)
        letters = string.ascii_lowercase
        str1 = ''
        str2 = ''
        for i in range(word_len1):
            str1 += random.choice(letters)
        for i in range(word_len2):
            str2 += random.choice(letters)
        yield f"{str1} {str2}"


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

