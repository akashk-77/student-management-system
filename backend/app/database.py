import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:root@localhost:3306/student_management"
)

print(f"DATABASE_URL = {repr(DATABASE_URL)}")

engine = create_engine(DATABASE_URL)
