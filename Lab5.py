# Задания 1: Программа, которая принимает список чисел и, с помощью множеств, определяет количество различных чисел внутри списка.
def cnt_varios_num(l_num):
    return len(set(l_num))

#Задание 2: Программа определяет является ли первое множество подмножеством второго, причем если множества совпадают, то ответ False
def is_subset(set_1,set_2):
    return set_1.issubset(set_2) and set_1 != set_2

#Задание 3: Маша и Саша играют в город
def cities_game(set_cities, city):
    if city in set_cities:
        return "REPEAT"
    else:
        return "OK"

list_a = list(map(int, input("Введите список чисел: ").split()))
print("Количество различных элементов списка: ", cnt_varios_num(list_a))
list_b = set(map(int, input("Введите первое множество чисел: ").split()))
list_с = set(map(int, input("Введите второе множество чисел: ").split()))
if is_subset(list_b, list_с):
    print("Да, первое множество является подмножеством второго")
else:
    print("Нет, первое множество не является подмножеством второго")

set_cities = set(map(str, input("Введите названные города: ").split()))
new_city = input("Введите название нового города: ")
print(cities_game(set_cities , new_city))






