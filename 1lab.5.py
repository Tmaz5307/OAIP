a = open("input.txt", encoding="utf-8")
b = 0
for line in a:
    b += len(line)
    c = b * 8
    d = b
    e = b / 1000
    f = e / 1000
    g = f / 1000
    h = g / 1000
print(c, "бит")
print(d, "байт")
print(e, "мегабайт")
print(f, "мегабайт")
print(g, "гигабайт")
print(h, "терабайт")
