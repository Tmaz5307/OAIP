n = int(input())
digs = [False] * 10
k = 0
for _ in range(n):
    n = int(input())
    while n:
        d = n % 10
        if not digs[d]:
            digs[d] = True
            k += 1
        n //= 10
print(k)
