# Реализуйте функцию get_hidden_card(), которая:
# Принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки
# Возвращает его скрытую версию, которую можно использовать на сайте для отображения
# Если исходная карта имела номер 2034399002125581, то скрытая версия выглядит так ****5581.
# Другими словами, функция заменяет первые 12 символов на звездочки.
# Количество звездочек регулируется вторым необязательным параметром. Значение по умолчанию — 4.
# # Кредитка передается внутрь как строка
# get_hidden_card('2034399002121100', 1)  # *1100
# get_hidden_card('1234567812345678', 2)  # **5678
# get_hidden_card('1234567812345678', 3)  # ***5678
# get_hidden_card('1234567812345678')     # ****5678

def get_hidden_card(number, count_stars = 4):
    print(f'{"*" * count_stars}{number[-4:]}')

get_hidden_card('2034399002121100', 1)
get_hidden_card('1234567812345678', 2)
get_hidden_card('1234567812345678', 3)
get_hidden_card('1234567812345678')
get_hidden_card('1234123412341234')