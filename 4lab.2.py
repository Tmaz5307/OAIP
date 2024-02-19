def template():
    a, b, c = int(input()), int(input()), int(input())
    if b == a == c:
        print('Равносторонний')
    elif a != b != c != a:
        print('Разносторонний')
    elif (a + b >= a + c) or (a + b <= a + c) or (c + b >= a + b) or (c + b <= a + b) or (c + a <= b + c) or (c + a >= b + c):
        print('Равнобедренный')
