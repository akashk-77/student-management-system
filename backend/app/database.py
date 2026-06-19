from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Goose22%402008.in@localhost/studentdb"

engine = create_engine(DATABASE_URL)