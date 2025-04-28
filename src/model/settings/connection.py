from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_connection import db_host, db_name, db_password, db_port, db_user


class DBConnectionHandler:

    def __init__(self)->None:

        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            db_user,
            db_password,
            db_host,
            db_port,
            db_name
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind = self.get_engine())
        self.session=session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        