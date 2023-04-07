# Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей
# в возрасте в виде The age difference is 11.

def get_age_difference(date_1, date_2):
    return f'The age difference is {abs(date_2 - date_1)}'

result = get_age_difference(2001, 2018)
print(result)