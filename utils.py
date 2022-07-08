import json
import datetime


def get_data_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_datetime(date: str) -> datetime.date:
    """Преобразование строки с датой в объект datetime"""
    month, day, year = date.split('/')
    return datetime.date(int(year), int(month), int(day))

# print(get_datetime("11/24/2022"))
