import argparse
import os

from config import cfg_database_dir
from src import models


def read_parameters() -> dict:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        '-o', '--option',
        required=True,
        help='options: create_database, ...'),
    args = vars(ap.parse_args())
    return args


def create_database():
    if not os.path.isdir(cfg_database_dir):
        os.makedirs(name=cfg_database_dir, exist_ok=True)
    # creating nutrients table
    if models.Nutrient.table_exists():
        models.Nutrient.drop_table()
    models.Nutrient.create_table()
    # creating costumers table
    if models.Customer.table_exists():
        models.Customer.drop_table()
    models.Customer.create_table()


if __name__ == '__main__':
    parameters: dict = read_parameters()
    option: str = parameters['option']
    if option == 'create_database':
        create_database()
