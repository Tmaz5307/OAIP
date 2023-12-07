a = int(input())
b = [int(input()) for e in range(a)]
c = sorted(set(b[i] - b[j] for i in range(a) for j in range(a)))
for d in c:
    print(d)
