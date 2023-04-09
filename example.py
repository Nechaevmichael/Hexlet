a = ' Y;lkj;lkj'
# a = a.strip()
for i in a:
    if i == ';':
        a.replace(i, '')
print(a) i