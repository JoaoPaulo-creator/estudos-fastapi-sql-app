from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

engine = create_engine(
    #  argumento check_same_thread é necessário somente para SQLite
    #  By default SQLite will only allow one thread to communicate with it,
    #  assuming that each thread would handle an independent request.
    SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
