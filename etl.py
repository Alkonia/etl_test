import os
import pandas
from constant import FILE_MODELS
from db.connection import DatabaseConnection
from utils import clean_column_name


class ETL:
    model = ""
    dir = ""
    db_connection = DatabaseConnection()

    def __init__(self, model):
        self.model = model
        self.dir = os.path.join("files", FILE_MODELS[model])

    def extract(self):
        self.file = pandas.read_csv(self.dir, encoding='ISO-8859-1', sep=';')
        print(f"Extract of {self.model} success")

    def transform(self):
        self.file.columns = [clean_column_name(
            col) for col in self.file.columns]
        self.file.columns = ['id'] + list(self.file.columns[1:])
        print(f"Transform of {self.model} success")

    def load(self):
        self.file.to_sql(name=self.model,
                         con=self.db_connection.engine, if_exists='append', index=False)
        print(f"Load of {self.model} success")

    def main(self):
        print(f"---ETL init of {self.model}---")
        self.extract()
        self.transform()
        self.load()
        print(f"---ETL success of {self.model}---")
        print("")
