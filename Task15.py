# Реализуйте функцию is_contains_char(). Она должна проверять, содержит ли строка указанную букву
# (вне зависимости от регистра). Функция принимает два параметра:
#
# Строка
# Буква для поиска
# И возвращает результат проверки – булево значение.
# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'h'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False

def is_contains_char(text, char):
    result = False
    i = 0
    while i < len(text):
        if text[i].lower() == char.lower():
            result = True
        i += 1
    return result
print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False