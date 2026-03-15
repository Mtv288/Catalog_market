import csv

from app.core.config import BASE_DIR
from app.core.constants import CSV_TO_DB, COLUMNS_LIST, TYPING_OBJ
from app.schemas.pydentic_schemas import GoodsSchema



path = BASE_DIR/"All.csv"


def get_data_in_csv(
        path: str,
        column: list[str],
        encoding: str = "cp1251",
        sep: str = ";"
):
    """
    Получение списка словарей с нужными колонками для преобразования для использования в бд
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


def typify_objects(data: list[dict], type_obj: dict) -> list[dict]:
    def conv(func, v):
        try:
            return func(v)
        except(ValueError, TypeError):
            return v

    return [
        {
            k: conv(type_obj[k], v) if k in type_obj and v not in (None, "") else v
                    for k, v in row.items()
        }
        for row in data
    ]


















def map_csv_rows_to_db(data: list[dict], new_key: str) -> list[dict]:
    """
    Преобразует список словарей из csv в список словарей для бд меняет ключи
    :param data: список словарей из csv
    :param new_key: список новых ключей для вставки в бд
    :return: список словарей с ключами для бд
    """


    list_validated = []
    for i in data:
        mapped = {k: v for k, v in zip(CSV_TO_DB, i.values())}
        validated = GoodsSchema(**mapped)
        list_validated.append(validated)
    print(list_validated)






#map_csv_rows_to_db(get_data_in_csv(path, COLUMNS_LIST), CSV_TO_DB)
d = get_data_in_csv(path, COLUMNS_LIST)
print(typify_objects(d, TYPING_OBJ))



