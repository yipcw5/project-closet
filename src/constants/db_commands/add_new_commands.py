'''
Constants containing SQL queries to my_closet: add_new module
'''

INSERT_INTO_CLOTHING_ENTRY = '''
INSERT INTO clothing_entry (%s) 
VALUES (%s) RETURNING clothing_id
'''

INSERT_INTO_DESCRIPTION_VALUES = '''
INSERT INTO description_values (category_id, description_value) 
VALUES (%s, %s)
RETURNING value_id;
'''

INSERT_INTO_DESCRIPTION_CATEGORIES_MAP = '''
INSERT INTO description_categories_map (clothing_id, value_id) VALUES
(%s, %s);
'''

SELECT_DESCRIPTION_CATEGORIES_NAMES = '''
SELECT category_name FROM description_categories
'''

'''
EXAMPLE ENTRY ADD

INSERT INTO clothing_entry (brand_name, clothing_subtype, date_bought) 
VALUES (%s, %s, %s) RETURNING clothing_id;

clothing_id = cur.fetchone()[0]

INSERT INTO description_values (category_id, description_value) VALUES
(1, 'Blue'),
(2, 'Flannel');

INSERT INTO description_categories_map (clothing_id, value_id) VALUES
(1, 1),
(1, 2);

'''
