def trim_and_repeat(text, offset = 0, repetitions = 1):
    slim = text[offset:]
    return slim * repetitions

print(trim_and_repeat('python', offset=3, repetitions=2)) # honhon
print(trim_and_repeat('python', repetitions=3))  # pythonpythonpython
print(trim_and_repeat('python'))  # python

# trim_and_repeat(text, offset=3, repetitions=2)  # honhon
# trim_and_repeat(text, repetitions=3)  # pythonpythonpython
# trim_and_repeat(text)  # python