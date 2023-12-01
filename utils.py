import json

from datetime import datetime

amount_of_elements_1 = 2
amount_of_elements_2 = 3

def get_data():
    """Получаем данные из файла"""
    with open('D:\py.projects\KP3\operations.json', 'r', encoding='utf-8') as file:
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
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        row['date'] = date
    return data

def mask_credit_card(card_number):
    visible_diggets = card_number[:6] + card_number[-4:]
    masked_card_number = ' '.join([visible_diggets[:4], visible_diggets[4:6], '** ', '****', visible_diggets[-4:]])
    return masked_card_number

def hidden_card(data):
    for row in data:
        card_number = row.get('from', '').split()
        if len(card_number) == amount_of_elements_1:
            row['from'] = card_number[0] + ' ' +  mask_credit_card(card_number[1])
        if len(card_number) == amount_of_elements_2:
            row['from'] = card_number[0] + ' ' + card_number[1] + ' ' + mask_credit_card(card_number[2])
    return data


def hidden_score(data):
    """Выводит в необходимом формате номер счета """
    for row in data:
        score = row.get('to', '').split()
        if len(score) == amount_of_elements_1:
            row['to'] = score[0] + ' **' + score[1][-4:]
        if len(score) == amount_of_elements_2:
            row['to'] = score[0] + score[1] + ' **' + score[2][-4:]
    return data













