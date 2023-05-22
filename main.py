# Практическое занятие №1
# Задание 1: функция принимает три числа и возвращает количество совпаюащих чисел
def cnt_equal_nums(x, y, z):
    cnt = 0
    if x == y:
        cnt += 1
    if x == z:
        cnt += 1
    if y == z:
        cnt += 1
    print("Количество совпадающих чисел среди введеных = ", cnt)
    return cnt


# Вспомогательная функция подсчета разрядов в числе для вывода треугольника в задании 2
def cnt_digit(x):
    cnt = 0
    while x > 0:
        x = x // 10
        cnt += 1
    return cnt


# Задание 2: вывод треугольника чисел. Реализация с использованием строк.
def print_triangle_use_string(n):
    s = ""
    for i in range(1, n + 1, 1):
        space = cnt_digit(n) - cnt_digit(i) + 1
        s += str(i) + space * " "
        print(s, end="\n")


# Задание 2: вывод треугольника чисел. Реализация с использованием чисел.
def print_triangle_use_num(n):
    for i in range(1, n + 1, 1):
        for j in range(1, i + 1, 1):
            print(j, end=(cnt_digit(n) - cnt_digit(j) + 1) * " ")
        print(" ")


# Задание 3: вывод пирамиды чисел. Реализация с использованием чисел.
def print_pyramid_use_num(n):
    cnt_n = cnt_digit(n) + 1
    for level in range(1, n + 1, 1):
        print(" " * (n - level) * cnt_n, end=" ")
        for i in range(1, level, 1):
            print(i, end=(cnt_n - cnt_digit(i)) * " ")
        for j in range(level, 0, -1):
            print(j, end=(cnt_n - cnt_digit(j)) * " ")
        print(" " * (n - level) * cnt_n)


n = int(input("Добро пожаловать! Введите целое число: "))
print("Вывод треугольника через строки. Разрядность введеного числа учитывается: ")
print_triangle_use_string(n)
print("Вывод треугольника через числа. Разрядность введеного числа  учитывается: ")
print_triangle_use_num(n)
print("Вывод пирамиды через числа: ")
print_pyramid_use_num(n)
print("Введите три целых числа. Программа вернет количество совпадающих чисел")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
cnt_equal_nums(x, y, z)
