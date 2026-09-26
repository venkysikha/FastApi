from datetime import datetime ,timedelta
from typing import Any ,Union
from sqlalchemy.orm import mapped ,mapped_column
from sqlalchemy import String ,Integer ,Boolean ,DateTime,func

from db.database import Base

# create a user model to represent the user table in the database 

class User(Base):
    __tablename__ ="users"
    id : mapped[int] = mapped_column(Integer,primary_key=True ,index = True)
    name : mapped[str] = mapped_column(String(50),nullable =False)
    email : mapped[str] = mapped_column(String(50),nullable =False,unique=True)
    passed : mapped[str] = mapped_column(String(100),nullable =False)
    is_active : mapped[bool] = mapped_column(Boolean,default=True)
    created_at : mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    
