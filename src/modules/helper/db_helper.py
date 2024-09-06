import psycopg2
from constants.errors import ERR_DB_CONN, ERR_DB_TABLES_INIT
from constants.db_commands.init_db import RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES

def init_db():
    '''Connect to db and initialise tables'''
    try:
        conn = psycopg2.connect(database="my_closet",
                                host="localhost",
                                user="choiwanyip",
                                password="",
                                port="5432")
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_CONN}: {e}")

    print("[INFO] Connection to My_Closet successful. Initiating tables...")
    cursor = conn.cursor()

    init_db_queries = [RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES]
    try:
        for query in init_db_queries:
            cursor.execute(query)
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_TABLES_INIT}: {e}")
    
    return conn, cursor
