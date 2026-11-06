text = input("Введите текст: ")

original_length = len(text)
words = text.split()
normalized = " ".join(words)

print(f"Исходная длина: {original_length}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized!r}")
print(f"Количество слов: {len(words)}")
