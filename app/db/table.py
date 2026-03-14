from datetime import date
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped,mapped_column
from .main_db import Base



class Goods(Base):

    __tablename__ = 'good'
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int]
    name: Mapped[str]
    count: Mapped[int] = mapped_column(Integer(), nullable=True)
    size: Mapped[int]
    price: Mapped[int]
    photo_path: Mapped[str] = mapped_column(String(), nullable=True)
    codeEAN: Mapped[int] = mapped_column(Integer(), nullable=True)


class User(Base):

    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    name: Mapped[str]
    date_register: Mapped[date]
    count_in_coming: Mapped[int]
    lost_date_incoming: Mapped[date]

