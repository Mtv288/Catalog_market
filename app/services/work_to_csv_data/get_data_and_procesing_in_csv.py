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
    """
    Здесь выбираем нужные столбцы из прочитанного csv и меняем на нужные типы данных
    :param data: Список словарей из csv в данном случае, можно любой list(dict)
     :param type_obj: словарь для мапинга типов
    :return: список словарей с нужными ключами и типами данных
    """
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


def









print(typify_objects(get_data_in_csv(path, COLUMNS_LIST), TYPING_OBJ))
#map_csv_rows_to_db(typify_objects(d, TYPING_OBJ), CSV_TO_DB)



