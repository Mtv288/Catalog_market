import csv
from app.core.config import BASE_DIR
from app.core.constants import CSV_TO_DB, COLUMNS_LIST



path = BASE_DIR/"All.csv"


def get_data_in_csv(
        path: str,
        column: list[str],
        encoding: str = "cp1251",
        sep: str = ";"
):
    """
    Получение списка словарей с нужными колонками для преоброзования  для использования в бд
    :param path: путь до файла CSV
    :param column: список нужных колонок из csv
    :param encoding: кодировка (по умолчанию cp1251)
    :param sep: параметр разделителя для csv (delimiter по умолчанию ";"
    :return: список словарей
    """

    data = []
    with open(path, encoding=encoding, newline="") as exp:
        reader = csv.DictReader(exp, delimiter=sep)

        for i in reader:
            data.append({col: i[col] for col in column})

    return data


def map_csv_rows_to_db(data: list[dict], new_key: str):
    """
    Преобразует список словарей из csv в список словарей для бд меняет ключи
    :param data: список словарей из csv
    :param new_key: список новых ключей для вставки в бд
    :return: список словарей с ключами для бд
    """

    list_value = []
    for i in data:
        for k, j in zip(new_key, i.values()):
            tmp = {k: j}
            list_value.append(tmp)
    return list_value


print(map_csv_rows_to_db(get_data_in_csv(path, COLUMNS_LIST), CSV_TO_DB))



