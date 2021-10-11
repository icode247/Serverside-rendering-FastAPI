from datetime import date
from pydantic import BaseModel

class Movie(BaseModel):
    id = int
    name = str
    desc = str
    type = str
    url = str
    rating = str
    data = date
    
    class Config:
        orm_mode = True