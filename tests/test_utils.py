import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert [x["state"] for x in data] == "EXECUTED"


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x['date'] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2018-06-30T02:08:58.425572", "2018-03-23T10:45:06.972075"]



def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    print(data)
