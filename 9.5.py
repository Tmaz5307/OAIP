try:
    a = int(input())
    b = int(input())
    c = a // b
except ZeroDivisionError:
    print("Деление на 0 невозможно")
except ValueError:
    print("Введите только целочисленные значения")
else:
    print(c)
finally:
    print("Выход из программы")