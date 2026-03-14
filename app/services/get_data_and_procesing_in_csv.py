import csv
from app.core.config import BASE_DIR
from app.core.constants import COLUMNS_LIST


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
            data.append(tuple(i[col] for col in column))

    return data

print(get_data_in_csv(path, COLUMNS_LIST))


