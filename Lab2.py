# Практическое занятие №2
# Вспомогательная функция подсчета разрядов в числе для вывода треугольника в задании 2
def cnt_digit(x):
    cnt = 0
    while x > 0:
        x = x // 10
        cnt += 1
    return cnt


# Задание 1: Треугольник Паскаля
def print_Paskal_triangle(n):
    triangle = []
    for i in range(0, n + 1):
        row_now = [1] * (i + 1)
        for j in range(0, i + 1):
            if j != 0 and j != i:
                row_now[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row_now)
    # Красивая печать треугольника Паскаля
    cnt_n = cnt_digit(triangle[n][n // 2])  # Элемент в треугольнике Паскаля с самым большим числом разрядов
    for i in range(0, n + 1):  # Цикл по строкам треугольника Паскаля
        print(" " * (n - i) * cnt_n,
              end=" ")  # Количество пробелов на каждой строке слева: глубина треугольника -1 и * на кол-во разрядов в самом большом числе треугольника Паскаля
        for j in range(0, i + 1):  # Цикл по элементам строки треугольника Паскаля
            print(triangle[i][j], end=" " * (cnt_n - cnt_digit(triangle[i][
                                                                   j])))  # Выводим элемент треугольника и если кол-во разрядов не совпадает с максимальным добавляем пробелы
            print(" " * cnt_n,
                  end="")  # После каждого элемента треугольника Паскаля надо оставить свободное место под один элемент с максимальным кол-во разрядов
        print(" " * (n - i) * cnt_n)  # Аналогично допечатываем пробелы справа


# Задание 2: найти все делители целого числа
def find_all_divider(x):
    dividers = []
    for i in range(x, 0, -1):
        if x % i == 0:
            dividers.append(i)
    print(dividers)
    return dividers

# Задание 3: вывести треугольник Серпинского:
def print_Serpinski_triangle(y):
    pattern = ["*"] # Лист, в котором мы храним элементы треугольника серпинского. Каждый элемент листа - это строка в треугольнике Серпинского.
    for i in range(y): # Цикл, в котором мы формируем элементы треугольника Серпинского
        space = " " * (2**i) # Пробел возле каждого элемента треугольника Серпинского. Коэффициент 2^i определяет размер пробела
        pattern = [space + x + space for x in pattern] + [x + " " + x for x in pattern] # Формируем i-ый треугольник Серпинского.
    print("\n".join(pattern)) # Распечатываем элементы треугольника, соединяя их через новую строку


n = int(input("Добро пожаловать! Введите целое число для вывода треугольника Паскаля: "))
print("Треугольника Паскаля указанной глубины: ")
print_Paskal_triangle(n)
x = int(input("Введите число, делители которого нужно найти: "))
find_all_divider(x)
y = int(input("Введите глубину треугольника Серпинского "))
print_Serpinski_triangle(y)