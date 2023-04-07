# Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы.
# Функция должна вернуть булево значение:

def has_upper_case(text) -> bool:
    result = False
    for i in text:
        if i == i.upper():
            result = True
    return result

print(has_upper_case("pyThoN"))