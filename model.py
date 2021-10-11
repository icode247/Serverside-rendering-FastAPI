from typing import Text
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class Movie(Base):
    __tablename__ = "Movie"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    desc = Column(Text())
    type = Column(String(20))
    url = Column(String(100))
    rating = Column(Integer)