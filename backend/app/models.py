from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    roll_no = Column(String(20))
    name = Column(String(100))
    department = Column(String(100))
    year_of_study = Column(Integer)
    email = Column(String(100))
    phone = Column(String(15))