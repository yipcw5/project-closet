"""
Add new item of clothing to my_closet db
[debugging purposes]
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

import os.path
from constants.errors import ERR_EMPTY_INPUT, ERR_INVALID_INPUT
from constants.messages import MSG_ADD_NEW_SUCCESS, MSG_MISSING_INPUT_OK, DEBUG_DESCRIPTION_CATEGORIES_MAP_ADDED, DEBUG_DESCRIPTION_VALUES_ADDED
from constants.db_commands.add_new_commands import INSERT_INTO_CLOTHING_ENTRY, SELECT_DESCRIPTION_CATEGORIES_NAMES, INSERT_INTO_DESCRIPTION_VALUES, INSERT_INTO_DESCRIPTION_CATEGORIES_MAP
from modules.helper.db_helper import execute_query, string_to_date
from .config import clothing_entry_columns

def add_new_main(conn):
    '''Add new clothing entry from scratch'''

    # User input: clothing_entry
    clothing_entry_values = input_clothing_entry_values(clothing_entry_columns)

    # Reformat clothing_entry_columns/values into SQL query string
    clothing_entry_columns_keys = ", ".join(clothing_entry_columns.keys())
    clothing_entry_values_string = "'" + "', '".join(clothing_entry_values) + "'"

    # Build + execute SQL query to add user input
    insert_into_clothing_entry_values = INSERT_INTO_CLOTHING_ENTRY % (clothing_entry_columns_keys, clothing_entry_values_string)
    clothing_id = execute_query(conn, insert_into_clothing_entry_values, 'one')
    print(MSG_ADD_NEW_SUCCESS.format("clothing_entry", clothing_id[0]))

    # User input: description_categories
    description_categories_names = execute_query(conn, SELECT_DESCRIPTION_CATEGORIES_NAMES, 'all')
    input_description_category_values(conn, description_categories_names, clothing_id)

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

def input_description_category_values(conn, description_categories_names, clothing_id):
    '''Obtain user input of description_category values to add'''
    for i, name in enumerate(description_categories_names):
        user_value = input(f"Insert {name[0]}s (separated by commas or leave blank): ")
        
        if not user_value:
            # If blank input, skip onto next category
            print(MSG_MISSING_INPUT_OK)
            continue

        try:
            user_value_arr = user_value.split(", ")
        except ValueError as e:
            raise ValueError(f"{ERR_INVALID_INPUT}: '{e}'") from e

        for value in user_value_arr:
            # Add to description_values e.g. (1, 'Blue')
            insert_into_description_values_query = INSERT_INTO_DESCRIPTION_VALUES % (i+1, f"'{value}'")
            value_id = execute_query(conn, insert_into_description_values_query, 'one')

            print(DEBUG_DESCRIPTION_VALUES_ADDED.format(value_id[0], value))

            # Add clothing_id-description_value_id pair e.g. (1, 1)
            insert_into_description_categories_map_query = INSERT_INTO_DESCRIPTION_CATEGORIES_MAP % (clothing_id[0], value_id[0])
            execute_query(conn, insert_into_description_categories_map_query)

            print(DEBUG_DESCRIPTION_CATEGORIES_MAP_ADDED.format(clothing_id[0], value_id[0]))
