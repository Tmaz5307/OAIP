a = [4, 6, 8, 9, 11, 23, 45]
b = 23
lol = 0
h = len(a) - 1
m = (lol + h) // 2
while b != a[m]:
    if b > a[m]:
        lol = m + 1
    else:
        h = m - 1
    m = (lol + h) // 2
print(m)
