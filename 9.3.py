a = int(input())
b = int(input())
try:
    c = a / b
except ZeroDivisionError:
    print("Деление на 0")
print(c)