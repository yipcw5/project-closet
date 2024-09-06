'''
Add new item of clothing
TODO: 
- change dependency of add_new_entry from INIT_TABLES string to actual db and check if tables and fields exist
- separate RESET_DB, INIT_TABLES as new module 'refresh'
'''

from constants.errors import ERR_INVALID_INPUT, ERR_EMPTY_INPUT
from constants.messages import MSG_ADD_NEW_OPTIONS
from constants.db_commands.init_db import INIT_TABLES

def add_new_main(conn, cursor):
    '''Add new clothing entry from scratch'''
    # Obtain INIT_TABLES constant accessible by word and skip entry of wear_count field
    field_values = []
    field_values = customise_query_by_line(field_values, INIT_TABLES, 'wear_count')
    print(field_values)
    

def customise_query_by_line(field_values, query_string, omitted_field):
    '''Split lines in query string, manipulate further and request user input'''
    query_fields = query_string.strip().splitlines()[1:-1]
    print(query_fields)
    for field_line in query_fields:
        # Remove leading/trailing spaces and commas then split words of query
        field_line = field_line.strip().rstrip(',')
        field_parts = field_line.split()

        # Convert field name into readable for user
        field_name = field_parts[0]
        if field_name == omitted_field:
            continue
        formatted_field_name = field_name.replace('_', ' ')

        field_value = input(f"Insert {formatted_field_name}: ")
        if not field_value and "NOT NULL" in field_line:
            # Require non-empty input if NOT NULL
            raise ValueError(ERR_EMPTY_INPUT)
    
        field_values.append(field_value)
    
    return field_values