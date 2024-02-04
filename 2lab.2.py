import json
data = {
    "Фамилия": "Кринжов",
    "Имя": "Артём",
    "Отчество": "Казулбекович",
    "Телефон": "88005553535",
    "Год рождения": "2077",
    "Город рождения": "Благовегас",
    "Место учёбы": "Академия «Арасака»",
}
with open("info.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
