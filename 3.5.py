a = int(input())
while True:
    if a == 0:
        break
    if a % 3 != 0 and a % 7 != 0:
        print(a)
    if a % 3 == 0 and a % 7 == 0:
        print('Караул!')
        break
    elif a % 3 == 0:
        print('Несчастливое')
    elif a % 7 == 0:
        print('Опасное')
    a = int(input())
