# Handles view of entries and properties for clothing items
# SETUP: open pgAdmin 4
import psycopg2
import pandas as pd
from constants.errors import ERR_DB_CONN

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
cursor.execute("CREATE TABLE * FROM my_closet")
print("ans: ", cursor.fetchone())
conn.close()

RESET_DB = '''
DROP TABLE IF EXISTS clothing_type, colours, dates_worn;
'''

INIT_TABLES = '''
CREATE TABLE clothing_entry(
    clothing_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL,
    clothing_type VARCHAR(50) NOT NULL,
    filename TEXT NOT NULL,
    date_bought DATE,
    wear_count INTEGER DEFAULT 0,
    is_exists BOOLEAN DEFAULT TRUE,
);

CREATE TABLE dates_worn(
    date_id SERIAL PRIMARY KEY,
    clothing_id INTEGER REFERENCES clothing_entry(clothing_id) ON DELETE CASCADE,
    date_worn DATE NOT NULL,
    season VARCHAR(50)
);

CREATE TABLE colours(
    colour_id SERIAL PRIMARY KEY,
    clothing_id INTEGER REFERENCES clothing_entry(clothing_id) ON DELETE CASCADE,
    colour VARCHAR(50) NOT NULL
);

CREATE TABLE description_category_names(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO description_category_names (category_name) VALUES ('Colour', 'Pattern', 'Other');

CREATE TABLE description_fields(
    description_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES description_categories(category_id) ON DELETE CASCADE;
);

CREATE TABLE clothing_descriptions (
    clothing_id INTEGER REFERENCES clothing_pieces(clothing_id) ON DELETE CASCADE,
    value_id INTEGER REFERENCES description_values(value_id) ON DELETE CASCADE,
    PRIMARY KEY (clothing_id, value_id)
);
'''

STARTER_CLOTHES = 'INSERT INTO clothing_entry (brand_name, clothing_type, date_bought) VALUES (%s) RETURNING id'
# clothing_id = cur.fetchone()[0]
STARTER_DESCRIPTION = 'INSERT INTO description_fields (clothing_id, category_id) VALUES (%s, %s) RETURNING id'
STARTER_DATES_WORN = 'INSERT INTO dates_worn (clothing_id, date)'
# sample execution: cur.execute(STARTER_DESCRIPTION, clothing_id, )