# Практическое занятие №3

# Вспомогательная функция для проверки на корректность ввода
def digit_in_s(s):
    for c in s:
        if c.isdigit():
            return True
    return False

# Задание №1: зашифровать строку
def string_ciper(s):
    if digit_in_s(s):
        print("Некорректный ввод данных. Строка не должна содержать цифры")
        return
    s += " "  # Добавляем символ пустой строки для корректной работы алгоритма
    cnt_previos_c = 1  # Количество вхождений предыдщего символа
    ciper_s = " "  # Будущая зашифрованная строка
    for c in s:
        if ciper_s[-1] == c:  # Если совпадает текущий с предыдушим
            cnt_previos_c += 1  # то просто увеличиваем кол-во вхождений
        else:  # Если не совпадает, то встретили новый символ
            if cnt_previos_c > 1:  # Если больше одного вхождения - добавляем к строке
                ciper_s += str(cnt_previos_c)
            ciper_s += c  # Добавляем новый встреченный символ к строке ciper_s
            cnt_previos_c = 1  # "объединичиваем" кол-во вхождений
    ciper_s.replace(" ", "")  # удаляем все пустые пробелы
    return ciper_s

# Задание 2: Расшифровка строки
def deciper_string(s):
    deciper_s = ""
    previos_is_digit = False
    cnt_c = "1"
    if not (s[0].isdigit()):
        for c in s:
            if c.isdigit() and not previos_is_digit:
                previos_is_digit = True
                cnt_c = c
            elif c.isdigit() and previos_is_digit:
                cnt_c += c
            else:
                if int(cnt_c) > 1:
                    deciper_s += deciper_s[-1] * (int(cnt_c)-1)
                deciper_s += c
                previos_is_digit = False
                cnt_c = "1"
    else:
        print("Некорректный ввод данных. Зашифрованная строка не может начинаться с цифр")
    return deciper_s

s1 = input("Введите строку для шифрования: ")
print("Зашифрованная строка:", string_ciper(s1))
s2 = input("Введите строку для дешифрования: ")
print("Дешифрованная строка:", deciper_string(s2))
