try:
    a = int(input())
    b = int(input())
    c = a + b
except ValueError:
    print("Введите только целочисленные значения")
else:
    print(c)
