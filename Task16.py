# Реализуйте функцию filter_string(). Она принимает на вход строку и символ и возвращает новую строку,
# в которой удален переданный символ во всех его позициях. Если строка не содержит указанный символ,
# то она возвращается без изменений.
# Итоговая строка также не должна содержать начальные и концевые пробелы:
# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win

def filter_string(text, char):
    text = text.strip()
    result = ''
    for i in text:
        if i.lower() != char.lower():
            result += i
    result = result.strip()
    return result

print(filter_string('If I look forward I win', 'i'))  # 'f  look forward  wn'
print(filter_string('If I look forward I win', 'O')) # 'If I lk frward I win