# # Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины.
# # Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:
#
# string = 'If I look back I am lost'
# print(my_substr(string, 1))  # => 'I'
# print(my_substr(string, 7))  # => 'If I lo'

def my_substr(string, length):
    result = ''
    i = 0
    while i < length:
        result += string[i]
        i += 1
    return result

print(my_substr('If I look back I am lost', 1))  # => 'I'
print(my_substr('If I look back I am lost', 7))  # => 'If I lo'