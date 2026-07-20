import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()