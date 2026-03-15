from _decimal import Decimal
from pydantic import BaseModel, condecimal
from datetime import date
from typing import Optional, Union


class GoodsSchema(BaseModel):

    code: int
    name: str
    count: int
    size: str
    price: Optional[Decimal] = Decimal('0')
    photo_path: str
    codeEAN: int


class User(BaseModel):
    id: int
    user_id: int
    name: str
    date_register:date
    count_in_coming: int
    lost_date_incoming: date
