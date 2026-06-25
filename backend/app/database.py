from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:password@localhost/studentdb"

engine = create_engine(DATABASE_URL)
