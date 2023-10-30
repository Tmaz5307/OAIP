a = int(input())
m1 = 0
m2 = 0
while abs(a) < 1000:
    if a > m1:
        m2 = m1
        m1 = a
    elif a > m2:
        m2 = a
    print(f'{m1=} {m2=}')
    a = int(input())
print(m1)
