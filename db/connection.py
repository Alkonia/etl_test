import os
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constant import DB_CONNECT
from db.base import BaseConnection
from utils import import_all_modules_from_folder


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            url = URL.create(**DB_CONNECT)
            cls._instance.engine = create_engine(url)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            cls.create_tables(cls._instance)
        return cls._instance

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.engine.dispose()

    def create_tables(self):
        import_all_modules_from_folder(os.path.join("db/models"))
        BaseConnection.metadata.drop_all(self.engine)
        BaseConnection.metadata.create_all(self.engine)
        print("Success tables creation")
