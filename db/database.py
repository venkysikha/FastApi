# in this file it contains the connection to the database 

from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker , declarative_base
from core.config import settings

# create the database  engine using the database url from the settings 

engine = create_engine(settings.Database_URL,pre_ping_pool= True)

# create the sessions to manage the database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class  for the models to follow the sqlalchemy orm structure
class Base(declarative_base()):
    pass


# create a session to manage the database transaction
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

