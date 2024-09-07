'''
Constants containing SQL queries to my_closet: initialisation
'''

INIT_TABLES = '''
CREATE TABLE IF NOT EXISTS clothing_entry(
    clothing_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL,
    clothing_subtype VARCHAR(50) NOT NULL,
    filename TEXT NOT NULL,
    date_bought DATE,
    wear_count INTEGER DEFAULT 0,
    date_removed DATE
);

CREATE TABLE IF NOT EXISTS dates_worn(
    date_id SERIAL PRIMARY KEY,
    clothing_id INTEGER REFERENCES clothing_entry(clothing_id) ON DELETE CASCADE,
    date_worn DATE NOT NULL,
    season VARCHAR(50)
);

-- e.g. Colour, Material; initiated only once
CREATE TABLE IF NOT EXISTS description_categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO description_categories (category_name) 
VALUES ('Colour'), ('Pattern'), ('Other')
ON CONFLICT (category_name) DO NOTHING;

-- Description terms e.g. Blue, Stripey
CREATE TABLE IF NOT EXISTS description_values(
    value_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES description_categories(category_id) ON DELETE CASCADE,
    description_value VARCHAR(50)
);

-- Assign description terms/values by description_category
CREATE TABLE IF NOT EXISTS description_categories_map (
    clothing_id INTEGER REFERENCES clothing_entry(clothing_id) ON DELETE CASCADE,
    value_id INTEGER REFERENCES description_values(value_id) ON DELETE CASCADE,
    PRIMARY KEY (clothing_id, value_id)
);
'''

INIT_FROM_CSV = '''
COPY clothing_entry (brand_name, clothing_subtype, filename, date_bought, date_removed) 
FROM '/Users/choiwanyip/Documents/GitHub/project-closet/src/databases/clothing_inventory.csv' 
DELIMITER ',' CSV HEADER;
'''

VIEW_CLOTHING_ENTRIES = '''
SELECT * FROM clothing_entry 
WHERE date_removed IS NULL
'''