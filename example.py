def string_or_not(value):
    if isinstance(value, str):
        return 'yes'
    else:
        return 'no'


print(string_or_not('Hexlet'))