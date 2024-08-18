# Handles view of entries and properties for clothing items
# User permissions: GRANT pg_read_server_files TO your_username;
import psycopg2
from constants.errors import ERR_DB_CONN
from constants.db_commands import *

# Initial db connection & cursor
try:
    conn = psycopg2.connect(database="my_closet",
                            host="localhost",
                            user="choiwanyip",
                            password="",
                            port="5432")
except:
    print(ERR_DB_CONN)

cursor = conn.cursor()

# Setup db tables from scratch

cursor.execute(RESET_DB)
cursor.execute(INIT_TABLES)
cursor.execute(INIT_FROM_CSV)
cursor.execute(VIEW_CLOTHING_ENTRIES)

print("ans: ", cursor.fetchall())
conn.close()