# Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару,
# значения которой расположены строго в порядке возрастания.
def sort_pair(pair):
    (first, second) = pair
    if first > second:
        return (second, first)
    return pair

print(sort_pair((5, 1)))