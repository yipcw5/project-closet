STARTER_CLOTHES = '''
INSERT INTO clothing_entry (brand_name, clothing_subtype, date_bought) 
VALUES (%s) RETURNING id'
'''
# clothing_id = cur.fetchone()[0]
STARTER_DESCRIPTION = '''
INSERT INTO description_fields (clothing_id, category_id) 
VALUES (%s, %s) RETURNING id'''
STARTER_DATES_WORN = 'INSERT INTO dates_worn (clothing_id, date)'
# sample execution: cur.execute(STARTER_DESCRIPTION, clothing_id, )

# Note: relative path is wrt src/main.py