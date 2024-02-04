import json
with open("info.json", "r", encoding="utf-8") as file:
    data = json.load(file)
a = input("Введите ключ для изменения:")
b = input(f"Введите новое значение для ключа {a}: ")
data[a] = b
with open("info.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
