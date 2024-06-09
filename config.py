# config.py

import os

class Config:
    # Example for SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///message_db.sqlite3'

    # Example for MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/message_db'

    # Example for PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/message_db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)




