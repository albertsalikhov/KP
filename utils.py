import json

from datetime import datetime


def get_data():
    """Получаем данные из файла"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_data(data):
    """Фильтруем, получаем только выполненные транзакции "EXECUTED"""
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, count_last_values):
    """Получаем последние 5 значений транзакций"""
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:5]
    return data


def get_formatted_data(data):
    """Форматирует и выводит список строк в требуемом формате """
    formatted_data = []
    for row in data:
        print(row['date'])
        date = datetime.strptime(row["date"], __format="%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        print(date)





        #data_split = date.split()#Здесь происходит разделение строки на слова по пробелам

        # num_list = [int(num) for num in filter(
           # lambda num: num.isnumeric(), data_split)] # проверяет слова, и список слов, с помощью генератора списка строки преобразовываются в целочисленный тип.


       # num = [int(i) for i in a if i.isdigit()]








