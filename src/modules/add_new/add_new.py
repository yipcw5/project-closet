'''
Add new item of clothing to my_closet db
'''

import os.path
from constants.errors import ERR_EMPTY_INPUT, ERR_INVALID_INPUT
from constants.messages import SUCCESS_MSG_ADD_NEW
from constants.db_commands.add_new_commands import INSERT_INTO_CLOTHING_ENTRY
from modules.helper.db_helper import execute_query, string_to_date
from .config import clothing_entry_columns

def add_new_main(conn):
    '''Add new clothing entry from scratch'''

    clothing_entry_values = input_clothing_entry_values(clothing_entry_columns)

    # Reformat clothing_entry_columns/values into SQL query string
    clothing_entry_columns_keys = ", ".join(clothing_entry_columns.keys())
    clothing_entry_values_string = "'" + "', '".join(clothing_entry_values) + "'"

    # Build + execute SQL query to add user input
    insert_into_clothing_entry_values = INSERT_INTO_CLOTHING_ENTRY % (clothing_entry_columns_keys, clothing_entry_values_string)
    clothing_entry_id = execute_query(conn, insert_into_clothing_entry_values, 'one')
    print(SUCCESS_MSG_ADD_NEW.format("clothing_entry", clothing_entry_id))

    # TODO: add user input for other tables, e.g. desc_categories

def input_clothing_entry_values(clothing_entry_cols):
    '''Obtain user input of clothing_entry values to add'''
    clothing_entry_values = []
    for column in clothing_entry_cols:
        # User input for each column name
        user_value = input(f"Insert {column}: ")
        
        if not user_value and clothing_entry_cols[column]:
            # If field is NOT NULL but user input is empty
            raise ValueError(f"{ERR_EMPTY_INPUT}: '{user_value}'")
        
        if column == "filename" and not os.path.isfile("./thumbnails/" + user_value):
            # Check if thumbnail file exists
            raise ValueError(f"{ERR_INVALID_INPUT}: '{user_value}' does not exist at /thumbnails/ directory")

        if column == "date_bought" and not string_to_date(user_value):
            # date format needs to follow rule
            raise ValueError(f"{ERR_INVALID_INPUT}: '{user_value}' does not follow format yyyy-mm-dd")
        
        clothing_entry_values.append(user_value)
    
    return clothing_entry_values

# Input this block straight into end of add_new_main for debugging purposes; undo-ing an insert immediately after
"""
    query = '''SELECT * FROM clothing_entry
    ORDER BY clothing_id DESC
    LIMIT 1;'''
    res = execute_query(conn, query, 'one')
    print("PROOF OF ADDITION: ", res)

    query2 = '''DELETE FROM clothing_entry
    WHERE clothing_id = (SELECT clothing_id FROM clothing_entry ORDER BY clothing_id DESC LIMIT 1);'''
    execute_query(conn, query2)
    print("DELETE SUCCESS")

    res = execute_query(conn, query, 'all')
    print("PROOF OF DELETION: ", res)
"""