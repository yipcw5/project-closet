# Handles view of entries and properties for clothing items
# SETUP: open pgAdmin 4
import psycopg2
import pandas as pd
from constants.errors import ERR_DB_CONN
from constants.db_commands import *

# Initial db connection & cursor
try:
    conn = psycopg2.connect(database="my_closet",
                            host="localhost",
                            user="yipcw",
                            password="",
                            port="5432")
except:
    print(ERR_DB_CONN)

cursor = conn.cursor()

# Setup db tables from scratch

cursor.execute(RESET_DB)
cursor.execute(INIT_TABLES)
cursor.execute(STARTER_CLOTHES)

print("ans: ", cursor.fetchone())
conn.close()