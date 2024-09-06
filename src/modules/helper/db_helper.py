import psycopg2
from constants.errors import ERR_DB_CONN, ERR_DB_TABLES_INIT
from constants.db_commands.init_db import INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES

def init_db():
    '''Connect to db and initialise tables'''
    try:
        conn = psycopg2.connect(database="my_closet",
                                host="localhost",
                                user="choiwanyip",
                                password="",
                                port="5432")
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_CONN}: {e}") from e

    print("[INFO] Connection to My_Closet successful. Initiating tables...")

    init_db_queries = [INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES]
    try:
        for query in init_db_queries:
            execute_query(conn, query)
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_TABLES_INIT}: {e}") from e
    
    return conn

def execute_query(conn, query, params='', fetch_option=''):
    '''Execute string query as SQL command'''
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        if not fetch_option:
            return
        elif fetch_option == "one":
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        return result