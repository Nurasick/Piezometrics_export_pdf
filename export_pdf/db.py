from config import DBConfig
import psycopg2

#Establishing simple connection to the db
def get_db_connection():
    config = DBConfig()
    try:
        conn = psycopg2.connect(
            host=config.postgres_host,
            port=config.postgres_port,
            user=config.postgres_user,
            password=config.postgres_password,
            dbname=config.postgres_db_name
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e
    