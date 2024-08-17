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
    date_removed DATE
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

# Note: relative path is wrt src/main.py
INIT_FROM_CSV = "COPY clothing_entry (brand_name, clothing_type, filename, date_bought, date_removed) FROM 'src/databases/clothing_inventory.csv' DELIMITER ',' CSV HEADER;"