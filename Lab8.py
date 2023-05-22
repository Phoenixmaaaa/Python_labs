import json
import csv


# Вспомогательная функция, чтобы получить названия столбцов таблицы CSV из лр 7
def get_headers(file_csv):
    headers = []
    with open(file_csv, "r", newline="") as file:
        headers = list(file.readline().split(","))
        file.close()
    headers[-1] = headers[-1].replace("\r\n", "")
    headers[-1] = headers[-1].replace("\n", "")
    return headers
# Вспомогательная функция, чтобы узнать необходимый размер для каждого столбца из лр 7
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
# Функция для вывода CSV в консоль из лр 7
def show(file_csv):
    headers = get_headers(file_csv)
    dict_lenghts = max_lenght_columns(file_csv)
    for header in headers:
        space = (dict_lenghts[header] - len(header)) * " "
        print(header, space, end="")
    print()
    with open(file_csv, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for header in headers:
                value = row[header]
                space = (dict_lenghts[header] - len(value)) * " "
                print(value, space, end="")
                if header == headers[-1]:
                    print()
# Считываем json file
name = "Sample-employee-JSON-data"
with open(name+".json", "r") as json_file:
    data_json = json.load(json_file)
# Перевод json -> CSV
with open(name+".csv", "w", newline='') as csv_file:
    headers = list(data_json["Employees"][0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for d in data_json["Employees"]:
        writer.writerow(d)
show("new.csv")
