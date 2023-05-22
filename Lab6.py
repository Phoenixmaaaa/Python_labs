#Практическая работа №6. Работа  с файлами.

#Задание 1: Считать из файла input_1.txt числа, записанные через пробел. Записать их произведение в output_1.tx
def multiply_num(path_to_file):
    res = 1
    with open(path_to_file, "r") as input_file:
       num_list = [int(x) for x in input_file.readline().split(" ")]
       for i in num_list:
           res *= i
       input_file.close()
    with open("output_1.txt","w") as output_file:
        output_file.write(str(res))
        output_file.close()
    print("Результат умножения чисел из первой строки файла", path_to_file, "сохранен в файл output_1.txt")

#Задание 2: Считать из файла input_2.txt числа, каждое записано на новой строке. Отсортированный список чисел записать в output_2.txt
def sort_num(path_to_file):
    res_list = []
    with open(path_to_file, "r") as input_file:
        num = input_file.readline()
        while num:
            res_list.append(int(num))
            num = input_file.readline()
        res_list.sort()
        input_file.close()
    with open("output_2.txt","w") as output_file:
        res_list_1 = "\n".join(map(str, res_list))
        output_file.write(res_list_1)
        output_file.close()
    print("Отсортированы числа из файла", path_to_file, "сохранены в файле output_2.txt")

#Задание 3: Дан файл со сведениями детей. Найти самого младшего и самого страшего ребенка  и записать информацию о них в отдельные файлы.
def find_kids (path_to_file):
    path_file_youngest = "The_youngest_kid.txt"
    path_file_oldest = "The_oldest_kid.txt"
    min_age = 200
    max_age = -1
    with open(path_to_file, "r") as input_file:
        info_kid = input_file.readline()
        while info_kid:
            age = -1
            if info_kid[-3].isdigit():
                age = info_kid[-3]+info_kid[-2]
                age = int(age)
            else:
                age = int(info_kid[-2])
            if age > max_age:
                max_age = age
                with open(path_file_oldest,"w") as file_oldest:
                    file_oldest.write(info_kid)
                    file_oldest.close()
            if age < min_age:
                min_age = age
                with open(path_file_youngest,"w") as file_youngest:
                    file_youngest.write(info_kid)
                    file_youngest.close()
            info_kid = input_file.readline()
        input_file.close()
        print("Самый старший ребенок записан в файле ",path_file_oldest,".Самый младщий в файле", path_file_youngest)

#Ввод пользовательских данных

str_nums_1 = input("Задание 1. Введите,через пробел, список чисел, которые хотите записать в input_1.txt: ")
path_to_file_1 = "input_1.txt"
#Запись пользовательских данных в файл
with open(path_to_file_1,"w") as input_file_1:
    input_file_1.write(str_nums_1)
    input_file_1.close()
multiply_num(path_to_file_1)

str_nums_2 = input("Задание 2. Введите, через пробел, список чисел, которые хотите записать в input_2.txt: ")
print("Предупреждение! В итоговом файле input_2.txt каждое новое число будет записано с новой строки, как того требует условие!")
str_nums_2 = str_nums_2.replace(" ", "\n")
path_to_file_2 = "input_2.txt"
with open(path_to_file_2,"w") as input_file_2:
    input_file_2.write(str_nums_2)
    input_file_2.close()
sort_num(path_to_file_2)

print("Задание 3. Данные взяты из файла kids_info.txt")
find_kids("kids_info.txt")



















