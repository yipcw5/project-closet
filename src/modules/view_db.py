# Handles view of entries and properties for clothing items
import psycopg2
from constants.messages import MSG_EMPTY_DB

def view_db():
    conn = psycopg2.connect(dbname="my_closet",
                            host="localhost",
                            user="yipcw",
                            password="password",
                            port="5432")
    print("[INFO] successfully established connection to db")

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * from cws_closet;")
        conn.commit()
    except:
        print("[INFO] db does not exist yet, creating one")

    # try:
        #cursor.execute("CREATE TABLE cws_closet (id INT PRIMARY KEY, brand TEXT, colour TEXT, clothing_type TEXT);")
        #conn.commit()
        cursor.execute("INSERT INTO cws_closet (brand, colour, type) VALUES (%s, %s, %s)", ("hollister", "navy", "parka"))
        conn.commit()
        print(cursor.fetchall())
    
    # except psycopg2.Error as e:
    #     # Rollback the transaction in case of an error
    #     conn.rollback()
    #     print("[ERROR]", e)

    finally:
        cursor.close()
        conn.close()

    return 0
