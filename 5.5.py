a = int(input())
b = [input() for _ in range(a)]
c = int(input())
for i in range(c):
    print(b[i % a])
