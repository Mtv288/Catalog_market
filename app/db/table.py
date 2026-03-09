from datetime import date
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped,mapped_column
from .main_db import Base



class Goods(Base):

    __tablename__ = 'good'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    count: Mapped[int] = mapped_column(Integer(), Nullable=True)
    size: Mapped[int] = mapped_column(Integer())
    price: Mapped[int] = mapped_column(Integer())
    photo_path: Mapped[str] = mapped_column(String(), Nullable=True)


class User(Base):

    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String())
    date_register: Mapped[date] = mapped_column(DateTime())
    count_in_coming: Mapped[int] = mapped_column(Integer())
    lost_date_incoming: Mapped[date] = mapped_column(DateTime())

