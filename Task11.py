# Реализуйте функцию get_number_explanation(), которая принимает на вход число и возвращает объяснение этого числа.
# Если для числа нет объяснения, то возвращается just a number. Объяснения есть только для следующих чисел:
# * 666 - devil number
# * 42 - answer for everything
# * 7 - prime number

def get_number_explanation(number) -> str:
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'

print(get_number_explanation(8))  # just a number
print(get_number_explanation(666))  # devil number
print(get_number_explanation(42))  # answer for everything
print(get_number_explanation(7))  # prime number