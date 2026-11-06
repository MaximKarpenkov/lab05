text = input("Введите текст: ")
cleaned = text.lower().replace(" ", "")

if not cleaned:
    print("Нет текста")
else:
    is_palindrome = True
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[-1 - i]:
            is_palindrome = False
            break
    print("Палиндром" if is_palindrome else "Не палиндром")
