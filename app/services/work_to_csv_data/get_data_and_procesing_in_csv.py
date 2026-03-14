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



rows = get_data_in_csv(path, COLUMNS_LIST)

def d (data):
    list_value = []
    for i in rows:
        temp_list = []
        for j in i.values():
            temp_list.append(j)
        list_value.append(temp_list)
    print(list_value)



d(rows)
def map_csv_rows_to_db(rows: List[Dict], key_mapping: Dict[str, str]):
    """
    Преобразует список словарей из csv в список словарей для бд меняет ключи
    :param rows: список словарей из csv
    :param key_mapping: {ключ из csv : имя колонки в бд}
    :return: список словарей с ключами для бд
    """






