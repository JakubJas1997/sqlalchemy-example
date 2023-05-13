from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer

Base = declarative_base()
login = "root"
password = "qwerty"
host = "localhost"
port = "3306"
dbname = "company"

engine = create_engine(f"mysql+pymysql://{login}:{password}@{host}:{port}/{dbname}")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)


Base.metadata.create_all(engine)