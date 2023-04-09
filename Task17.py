# Реализуйте функцию is_palindrome(), которая принимает на вход слово, определяет, является ли оно палиндромом,
# а затем возвращает логическое значение.

def is_palindrome(word):
    result = True
    if len(word) == 0 or len(word) == 1:
        result = True
    else:
        j = -1
        i = 0
        while i < len(word) // 2:
            if word[i] != word[j]:
                result = False
                break
            i += 1
            j -= 1
    return result

# print(is_palindrome(''))
print(is_palindrome('ишак ищет у тещи каши'))