a = (int(input()))


def max_chislo(a, maxc):
    b = a % 10
    if b > maxc:
        maxc = b
    if a > 9:
        return max_chislo(a // 10, maxc)
    return maxc


print(max_chislo())