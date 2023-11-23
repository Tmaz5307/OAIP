a = [4, 2, 1, 6, 3, 5]
for i in range(1, len(a)):
    b = a[i]
    j = i - 1
    while j >= 0 and a[j] > b:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = b
print(a)
