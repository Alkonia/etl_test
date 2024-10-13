from etl import ETL
from constant import MODELS


def main():
    for _, model in MODELS.items():
        etl_instance = ETL(model)
        etl_instance.main()


main()
