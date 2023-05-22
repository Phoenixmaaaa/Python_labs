# Задание 0: задан список с числами. Напишите программу, которая выводит все элементы списка, которые больше предыдущего, в виде отдельного списка
# Пример: 153237281 -> 5378
def higher_list(l_fisrt):
    len_first = len(l_fisrt)
    res_list = [l_fisrt[x] for x in range(1, len_first) if l_fisrt[x - 1] < l_fisrt[x]]
    return res_list


# Задание 1: задан список с числами. Вернуть список, где максимальный и минимальный элемент поменяли местами.
# Пример: 10,45,8,9,0,12 -> 10,0,8,9,45,12
def swap_max_min_l(l):
    max_el_l = max(l)
    min_el_l = min(l)
    max_index_l = l.index(max_el_l)
    min_index_l = l.index(min_el_l)
    l[max_index_l] = min_el_l
    l[min_index_l] = max_el_l
    return l


# Задание 2: заданы списки с числами, вернуть кол-во совпадающих элементов. Пусть СОВПАДАЮЩИЕ элементы имеют одинаковые индексы и значения. Пример:
# A: 1 1 1 1
# B: 1 1 2
# Совпадающих элементов -  2
def cnt_same_el(l_first, l_second):
    cnt = 0
    len_min = min(len(l_first), len(l_second))
    for i in range(0, len_min):
        if l_first[i] == l_second[i]:
            print("Индекс:",i,"Элемент: ",l_first[i])
            cnt += 1
    return cnt


# Задание 3 задан список строк. Вывести кол-во повторений данных строк в списке
# Пример: ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc'] -> 3 1 2 1
def cnt_same_str(l_str):
    d_str = dict()
    for c in l_str:
        if c in d_str:
            d_str[c] += 1
        else:
            d_str[c] = 1
    return d_str

list_a = list(map(int, input("Введите первый список чисел: ").split()))
print("Все элементы списка, которые больше предыдущего, в виде отдельного списка:\n", higher_list(list_a))
print("Максимальный и минимальный элементы введеного списка поменяны местами: ", swap_max_min_l(list_a))
list_b = list(map(int, input("Введите второй список чисел: ").split()))
print("Количество совпадающих элементов (и индекс, и значение одинаково) первого введеного списка и второго: = ", cnt_same_el(list_a, list_b))
list_str = input("Введите список строк: ").split()
print("Количество повторний строк в списке: ", cnt_same_str(list_str))
