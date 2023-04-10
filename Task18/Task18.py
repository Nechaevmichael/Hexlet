# Реализуйте функцию count_vowels(), которая принимает строку, считает и возвращает количество гласных букв в ней.
#
# Для проверки, является ли буква гласной, импортируйте и используйте функцию is_vowel() из модуля symbols.py.

import symbols

def count_vowels(text):
    count = 0
    for i in text:
        # print(symbols.is_vowel(i))
        if symbols.is_vowel(i):
            count += 1
    return count

print(count_vowels('One'))
print(count_vowels('London is the capital of Great Britain'))