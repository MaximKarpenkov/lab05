text = input("Введите строку: ")

words = text.split()
count = 0

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned:
        continue

    # Условие варианта 6: длина равна 4
    if len(cleaned) == 4:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")
