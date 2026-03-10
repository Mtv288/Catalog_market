from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import  DeclarativeBase
import  os
from dotenv import load_dotenv


class Base(DeclarativeBase):
    pass

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

async def get_db():
   async with SessionLocal() as session:
       try:
           yield session
       except:
           await session.rollback()
           raise
