'''
Constants containing SQL queries to my_closet: 
viewing by levels (clothing type, sub-type, individual piece)
'''

VIEW_CLOTHING_ENTRIES_BY_SUBTYPE = ' AND clothing_subtype IN (%s)'
VIEW_TABLE_COUNT = '''
SELECT COUNT(*) FROM clothing_entry 
WHERE date_removed IS NULL
'''
