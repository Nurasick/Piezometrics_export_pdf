from dotenv import load_dotenv
import os

load_dotenv()

class DBConfig:
    def __init__(self):
        #Загрузка конфигурации из .env
        self.postgres_host = os.getenv('POSTGRES_HOST')
        self.postgres_port = int(os.getenv('POSTGRES_PORT'))
        self.postgres_user = os.getenv('POSTGRES_USER')
        self.postgres_password = os.getenv('POSTGRES_PASSWORD')
        self.postgres_db_name = os.getenv('POSTGRES_DB_NAME')

        if not self.postgres_host:
            raise ValueError("POSTGRES_HOST is not set in .env")
        if not self.postgres_port:
            raise ValueError("POSTGRES_PORT is not set in .env")
        if not self.postgres_user:
            raise ValueError("POSTGRES_USER is not set in .env")
        if not self.postgres_password:
            raise ValueError("POSTGRES_PASSWORD is not set in .env")
        if not self.postgres_db_name:   
            raise ValueError("POSTGRES_DB_NAME is not set in .env")