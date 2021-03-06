import os
import dotenv
from peewee import SqliteDatabase, PostgresqlDatabase

dotenv.load_dotenv()

IS_DEBUG = True if os.environ.get('DEBUG') == '1' else False

TG_TOKEN = os.environ.get('TG_TOKEN_DEV') if IS_DEBUG else os.environ.get('TG_TOKEN')

SQLITE_NAME = 'test.db'
POSTGRES_CONFIG = {
    'host': 'localhost',
    'database': 'bot',
    'user': 'postgres'
}
DB = SqliteDatabase(SQLITE_NAME) if IS_DEBUG else PostgresqlDatabase(**POSTGRES_CONFIG)
