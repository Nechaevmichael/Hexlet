# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку и
# возвращает получившуюся строку:
# join_numbers_from_range(1, 1)  # '1'
# join_numbers_from_range(2, 3)  # '23'
# join_numbers_from_range(5, 10)  # '5678910'

def join_numbers_from_range(num_1, num_2):
    result = ''
    i = num_1
    while i <= num_2:
        result += str(i)
        i += 1
    return result

print(join_numbers_from_range(5, 10))