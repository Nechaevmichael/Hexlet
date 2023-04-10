# Реализуйте функцию choice_from_range(), которая принимает строку-набор и возвращает случайный символ по индексу
# из ограниченного диапазона.
#
# Аргументы функции:
#
# строка-набор
# начальный индекс диапазона
# конечный индекс диапазона
from random import randint

def choice_from_range(text, start, finish):
    char = randint(start, finish)
    return text[char]

print(choice_from_range('abcdef', 3, 5))