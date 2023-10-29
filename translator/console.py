def get_parameters():
    word = input("Введите слово для перевода ")

    print("Выбирите направление перевода")
    print("1. С английского на русский")
    print("2. С русского на английский")
    direction = input()
    if not direction:
        direction = 1
    direction = int(direction)
    return word, direction

def print_translation(word, translation):
    if translation:
        print(f"Перевод слова {word} - {translation}")
    else:
        print(f"Нет перевода для слова {word}")