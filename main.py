from utils import get_data, get_last_values, get_filtered_data, get_formatted_data, hidden_card, hidden_score


def main():
    COUNT_LAST_VALUES = 5

    data = get_data()
    data = get_filtered_data(data)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    data = hidden_card(data)
    data = hidden_score(data)
    print('INFO: вывод транзакций...')
    for row in data:
        print(row, end='/n/n')


if __name__ == '__main__':
    main()

