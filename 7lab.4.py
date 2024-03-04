def prostoe_chislo(a, b=None):
    if b is None:
        b = a - 1
    while b >= 2:
        if a % b == 0:
            print("Не простое число")
            return False
        else:
            return prostoe_chislo(a, b - 1)
    else:
        print("Простое число")
        return True


c = int(input())
prostoe_chislo(c)
