import csv


def read_csv_1c(file_path, needed_columns=None, encoding="cp1251"):
    """
    Читает CSV из 1С и возвращает список словарей с нужными колонками.

    :param file_path: путь к CSV файлу
    :param needed_columns: список колонок, которые нужно взять (по умолчанию все)
    :param encoding: кодировка файла (по умолчанию cp1251)
    :return: список словарей с данными
    """
    data = []

    with open(file_path, encoding=encoding, newline='') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar='"')

        # Если нет нужных колонок, берём все
        if needed_columns is None:
            needed_columns = reader.fieldnames

        for row in reader:
            clean_row = {}
            for col in needed_columns:
                value = row.get(col)
                if value is not None:
                    value = value.strip()  # чистим пробелы
                clean_row[col] = value
            data.append(clean_row)

    return data


csv_file = "../All.csv"
needed_columns = ["code","name","price","quantity","Размер","photo","scan_"]

data = read_csv_1c(csv_file, needed_columns)

# Проверим первые 5 строк
for row in data[:5]:
    print(row)