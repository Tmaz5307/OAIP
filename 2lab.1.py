import json
with open("test.json", "r", encoding="utf-8") as file:
    data = json.load(file)
c = [key for key in data if data[key]['city'] == 'Moscow']
if c:
    a = [data[person]['age'] for person in c]
    b = sum(a) // len(a)
    print("Средний возраст:", b)
    for key in data:
        if data[key]['city'] == 'Moscow':
            print("Имя:", data[key]["name"])
