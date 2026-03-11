import pandas as pd
from app.core.config import BASE_DIR

csv_file = BASE_DIR / "All.csv"
dt = pd.read_csv(csv_file, encoding='cp1251', nrows=1)

print(dt)