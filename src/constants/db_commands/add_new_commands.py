'''
Constants containing SQL queries to my_closet: add_new module
'''

INSERT_INTO_CLOTHING_ENTRY = '''
INSERT INTO clothing_entry (%s) 
VALUES (%s) RETURNING clothing_id
'''

# clothing_id = cur.fetchone()[0]
STARTER_DESCRIPTION = '''
INSERT INTO description_fields (clothing_id, category_id) 
VALUES (%s, %s) RETURNING id'''
STARTER_DATES_WORN = 'INSERT INTO dates_worn (clothing_id, date)'
# sample execution: cur.execute(STARTER_DESCRIPTION, clothing_id, )

# Note: relative path is wrt src/main.py