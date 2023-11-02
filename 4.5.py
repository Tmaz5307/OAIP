a = int(input())
m = 0
for i in range(1, a + 1):
    if a % i == 0:
        m += i
print(m)
