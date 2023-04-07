# Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных.
# Она принимает адрес сайта и возвращает его с https:// в начале.
# Функция принимает адреса в виде:
# АДРЕС
# http://АДРЕС
# https://АДРЕС (нормализованный)
# Функция всегда возвращает адрес в виде https://АДРЕС.

def normalize_url(addres):
    if addres[:6] == 'https:':
        return addres
    elif addres[:5] == 'http:':
        return f'https{addres[4:]}'
    else:
        return f'https://{addres}'

print(normalize_url('https://ya.ru'))  # https://ya.ru
print(normalize_url('google.com'))  # https://google.com
print(normalize_url('http://ai.fi'))  # https://ai.fi