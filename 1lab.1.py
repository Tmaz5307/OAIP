import random

with open("lines.txt", encoding="utf-8") as file:
    lines = file.readlines()
    if lines:
        print(random.choice(lines).strip())
    else:
        print("Пустой файл")
