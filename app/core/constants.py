# Константа для выборки нужных столбцов из csv файла #
COLUMNS_LIST = ["code", "name", "quantity", "Размер", "price", "photo", "scan_"]

# Константа для маппинга названий колонок из csv в модель таблицы
CSV_TO_DB = [
    "code",
    "name",
    "count",
    "size",
    "price",
    "photo_path",
    "codeEAN"
]

# Константа для принудительной типизации обьектов
TYPING_OBJ = [["code", "quantity", "scan_"], ["price"]]



