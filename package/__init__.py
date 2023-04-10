# Добавьте в __init__.py константу GREETING, которая должна содержать результат применения функции greet()
# к константе NAME. И та, и другая функция импортируются из модулей пакета в блоке импортов модуля __init__.py.
import package.functions
from package.functions import greet
from package.names import NAME

GREET = package.functions.greet(package.names.NAME)
print(GREET)