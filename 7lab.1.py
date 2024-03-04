def fact(a):
    if a > 1:
        return a * fact(a - 1)
    else:
        return 1


b = int(input())
print(fact(b))
