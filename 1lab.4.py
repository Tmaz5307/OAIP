a = open("words.txt", encoding="utf-8")
b = a.read().split()
print(max(b))
