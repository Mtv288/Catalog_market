from pydantic import BaseModel, condecimal
from datetime import date
from typing import Optional, Union


class GoodsSchema(BaseModel):
    id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = ""
    count: Optional[str] = None
    size: Optional[Union[int, str]] = ""
    price: Optional[str] = None
    photo_path: Optional[str] = None
    codeEAN: Optional[str] = None


class User(BaseModel):
    id: int
    user_id: int
    name: str
    date_register:date
    count_in_coming: int
    lost_date_incoming: date
