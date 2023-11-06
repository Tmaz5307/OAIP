a = [input()]
while a[-1] != 'стоп':
    a.append(input())
print(sorted(a[:-1], key=len)[0])
