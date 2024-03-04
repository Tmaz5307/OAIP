def recurs(n):
    if n == 1 or n == 2:
        return 1
    return recurs(n - 1) + recurs(n - 2)


n = int(input())
print(recurs(n))
