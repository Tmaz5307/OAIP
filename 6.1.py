a = 5
b = [4, 3, 2, 5, 1]
i = 0
while i < a - 1:
    j = 0
    while j < a - 1 - i:
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
        j += 1
    i += 1
print(b)
