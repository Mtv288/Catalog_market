# Здесь я создаю класс для работы с csv файлом котрый будет обрабатывать и обновлять данные в бд

from sqlalchemy import text
from app.db.main_db import engine
from app.core.config import BASE_DIR


class CSVProductImporter:
    def __init__(self, csv_file_name, column_map):
        """
        column_map = {
            "csv_sku": "sku",
            "csv_name": "name",
            "csv_price": "price",
            "csv_stock": "stock"
            }
        """
        self.csv_file = BASE_DIR / csv_file_name
        self.column_map = column_map

        self.csv_columns = list(column_map.keys())
        self.dp_columns = list(column_map.values())

        self.csv_sku = self.csv_columns[0]
        self.csv_stock = self.csv_columns[-1]

    async def run(self):
        """
        Основной метод для полной синхронизации
        """
        async with engine.begin() as conn:
            await self._create_staging(conn)
            await self._copy_csv(conn)
            await self._save_stock_history(conn)
            await self._upset_products(conn)
            await self._zero_missing_products(conn)

    async def _create_staging(self, conn):
        columns = ", ".join(f"{c} text" for c in self.csv_columns)
        await conn.execute(text(f"""
        CREATE TEMP TABLE staging_products({columns})"""))

    async def _copy_csv(self, conn):
        csv_cols = ", ".join(self.csv_columns)
        await conn.execute(text(f"""
            COPY staging_products ({csv_cols}) 
            FROM '{self.csv_file}' 
            WITH (FORMAT csv, HEADER trye)"""))

    async def _save_stock_history(self,conn):
        """
        Тут сохраняем всю историю изменений
        """
        await conn.execute(text(f"""
            INSERT INTO product_stock_history (sku, old_stock, new_stock, changed_at) 
            SELECT 
                p.sku, 
                p.stock, 
                s.{self.csv_stock}::int, 
                NOW() 
            FROM products p 
            JOIN staging_products s 
                ON p.sku = s.{self.csv_sku} 
            WHERE p.stock != s.{self.csv_stock}::int"""))

    async def _upset_products(self, conn):
        """
        Тут добавление новых товаров и удаление старых
        """
        csv_cols = ", ".join(self.csv_columns)
        db_cols = ", ".join(self.dp_columns)
        updates = ", ".join(f"{c}" for c in self.dp_columns if c != "sku")

        await conn.execute(text(f"""
            INSERT INTO products ({db_cols}) 
            SELECT {csv_cols} FROM staging_products 
            WHERE {self.csv_stock}::int > 0 
            ON CONFLICT (sku) DO UPDATE 
            SET {updates}
        """))

    async def _zero_mising_products(self, conn):
        """
        Обнуляем товары которых нет в csv и сохраняем историю
        """
        await conn.execute(text(f"""
            INSERT INTO product_stock_history (sku, old_stock, new_stock, changed_at) 
            SELECT sku, stock, 0, NOW() 
            FROM products 
            WHERE sku NOT IN (SELECT {self.csv_sku} FROM staging_products) 
                AND stock != 0 
            """))

        await conn.execute(text(f"""
            UPDATE products 
            SET stock = 0 
            WHERE sku NOT IN (SELECT {self.csv_sku} FROM staging_products) 
        """))

