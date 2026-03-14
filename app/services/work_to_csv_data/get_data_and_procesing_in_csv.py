import csv
from app.core.config import BASE_DIR
from typing import List, Dict
from app.core.constants import CSV_TO_DB, COLUMNS_LIST



path = BASE_DIR/"All.csv"


def get_data_in_csv(
        path: str,
        column: list[str],
        encoding: str = "cp1251",
        sep: str = ";"
):

    data = []

    with open(path, encoding=encoding, newline="") as exp:
        reader = csv.DictReader(exp, delimiter=sep)

        for i in reader:
            data.append({col: i[col] for col in column})

    return data

def get_values_in_dict(data: List[Dict]):
    new_list = []
    for i in data:
        print(type(i))
        data_temp = []
        for j in i:
            j.g
            print(g)



    return new_list

f = get_values_in_dict(get_data_in_csv(path, COLUMNS_LIST))



def map_csv_rows_to_db(rows: List[Dict], key_mapping: Dict[str, str]):
    """
    Преобразует список словарей из csv в список словарей для бд меняет ключи
    :param rows: список словарей из csv
    :param key_mapping: {ключ из csv : имя колонки в бд}
    :return: список словарей с ключами для бд
    """






