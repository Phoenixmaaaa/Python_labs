# Практическео занятие №7. Итоговая работа. CSV - файлы.
import csv
import random
from os import mkdir, listdir, getcwd


# Вспомогательная функция для генерации случайных чисел
def get_random_list(cnt_num, f_num, l_num):
    res = [random.randint(f_num, l_num) for x in range(0, cnt_num)]
    return res


# Вспомогательная функция, чтобы получить названия столбцов таблицы CSV
def get_headers(file_csv):
    headers = []
    with open(file_csv, "r", newline="") as file:
        headers = list(file.readline().split(","))
        file.close()
    headers[-1] = headers[-1].replace("\r\n", "")
    headers[-1] = headers[-1].replace("\n", "")
    return headers


# Вспомогательная функция, чтобы узнать необходимый размер для каждого столбца
def max_lenght_columns(file_csv):
    headers = get_headers(file_csv)
    dict_lenghts = dict()
    for header in headers:
        dict_lenghts[header] = len(header)
    with open(file_csv, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for header in headers:
                value = row[header]
                if dict_lenghts[header] < len(value):
                    dict_lenghts[header] = len(value)
        file.close()
        return dict_lenghts


# Вспомогательная функция для подсчета кол-во строк в CSV файле
def cnt_rows(file_csv):
    count = 0
    with open(file_csv, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            count += 1
    return count


# Задание 1. Написать функцию show, которая будет выводить в консоль файл CSV.
def show(file_csv, n_rows, flag):
    all_flags = ["top", "bottom", "random"]
    if flag not in all_flags:
        print("Введеный режим вывода не обнаружен")
        return
    headers = get_headers(file_csv)
    dict_lenghts = max_lenght_columns(file_csv)
    amt_rows = cnt_rows(file_csv)
    random_rows = get_random_list(n_rows, 1, amt_rows)
    for header in headers:
        space = (dict_lenghts[header] - len(header)) * " "
        print(header, space, end="")
    print()
    count = 1
    with open(file_csv, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for header in headers:
                value = row[header]
                space = (dict_lenghts[header] - len(value)) * " "
                if flag == "top" and count <= n_rows:
                    print(value, space, end="")
                    if header == headers[-1]: print()
                elif flag == "bottom" and count > amt_rows - n_rows:
                    print(value, space, end="")
                    if header == headers[-1]: print()
                elif flag == "random" and count in random_rows:
                    print(value, space, end="")
                    if header == headers[-1]: print()
            count += 1
        file.close()


# Задание 2. Написать функцию info, которая будет выводить кол-во строк в файле и статистику по столбцам:
def info(file_csv):
    headers = get_headers(file_csv)
    stat_col = dict()
    for header in headers:
        stat_col[header] = 0
    with open(file_csv, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for header in headers:
                value = row[header]
                if value != '':
                    stat_col[header] += 1
        file.close()
    print("Общее количество строк в файле ", file_csv, " = ", cnt_rows(file_csv))
    print("Статистика ненулевых строк в каждом столбце: ")
    print(stat_col)


#Задание 3: Написать функцию delNaN, удаляющая те строки таблицы, в которых есть пустые ячейки:
def delNaN(file_csv):
    with open(file_csv, 'r',newline="") as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if '' in row:
                data.remove(row)
        f.close()
    with open(file_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()

#Задание 4: Написать функцию MakeDS, которая случайным образом делит данные (строки) в соотношении 70\30:
def MakeDS(file_csv):
    with open(file_csv, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        learning_data = data[:int(len(data) * 0.7)]
        test_data = data[int(len(data) * 0.7):]
        f.close()
    if 'Learning' not in listdir(f'{getcwd()}') and 'Testing' not in listdir(f'{getcwd()}'):
        mkdir('Learning')
        mkdir('Testing')
    with open('Learning/l.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(learning_data)
        f.close()
    with open('Testing/t.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(test_data)
        f.close()

show("Titanic.csv",10,"top")
info("Titanic.csv")
delNaN("Titanic.csv")
MakeDS("Titanic.csv")

