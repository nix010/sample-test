import os

import pandas as pd
from sqlalchemy_utils import database_exists, create_database


def seed_data(database_url):
    exist = pd.read_sql('select * from clubs limit 1', database_url)
    if exist.empty:
        print('seed data in empty table clubs')
        clubs = pd.read_csv('./clubs.csv').reset_index(drop=True)
        clubs.to_sql('clubs', database_url, if_exists='append', index=False)


def create_db(database_url):
    if not database_exists(database_url):
        create_database(database_url)


if __name__ == '__main__':
    DATABASE_URL = os.getenv('DATABASE_URL')
    create_db(DATABASE_URL)
    seed_data(DATABASE_URL)
