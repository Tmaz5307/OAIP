N = int(input()) # кол-во макс. значений массива
a = [int(input()) for i in range(N)] # элементы  массива
b = a.count(max(a))
print(b)
