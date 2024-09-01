'''
Handles view of entries and properties for clothing items
User permissions: GRANT pg_read_server_files TO your_username;
'''

import psycopg2
from src.constants.errors import ERR_INVALID_INPUT, ERR_DB_CONN, ERR_DB_TABLES_INIT, ERR_DB_QUERY
from src.constants.messages import MSG_DB_VIEWER
from src.constants.db_commands.init_db import RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES
from src.constants.db_commands.view_by_entry import VIEW_CLOTHING_ENTRIES_BY_SUBTYPE, VIEW_TABLE_COUNT
from src.objects.clothing import ClothingEntry
from src.modules.view_db.config import view_db_config_template, clothing_type_to_sub_dict

def view_db_main():

    # Initialise db and tables
    try:
        conn, cursor = init_db()
    except Exception as e:
        print(e)
        return 1

    view_db_config = view_db_config_template
    view_db_config['clothing type']['category_list'] = clothing_type_to_sub_dict.keys()
    keys_list = list(view_db_config.keys())

    # Take user through levels of categories (viewing_type)
    for i, viewing_type in enumerate(view_db_config.keys()):
        category_list = view_db_config[viewing_type]['category_list']
        try:
            chosen_category = view_db_by_level_all(cursor, view_db_config, viewing_type, category_list)
        except ValueError or Exception as e:
            print(e)
            return 1
        
        if i < 2: 
            next_key = keys_list[i+1]
            category_list, next_query = view_db_by_level_spec(cursor, view_db_config, viewing_type)
            view_db_config[next_key]['query'] = next_query
            view_db_config[next_key]['search_value'] = chosen_category
            view_db_config[next_key]['category_list'] = category_list

    # Query & collate data on chosen clothing item
    try:
        chosenClothingItem = query_to_class_chosen_item(cursor, view_db_config)
    except Exception as e:
        print(e)
        return 1
    print(chosenClothingItem)

    conn.close()
    return 0

def init_db():
    # Connect to db
    try:
        conn = psycopg2.connect(database="my_closet",
                                host="localhost",
                                user="choiwanyip",
                                password="",
                                port="5432")
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_CONN}: {e}")

    print("[INFO] Connection to My_Closet successful. Initiating tables...")
    cursor = conn.cursor()

    # Initiate tables
    init_db_queries = [RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES]
    try:
        for query in init_db_queries:
            cursor.execute(query)
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_TABLES_INIT}: {e}")
    
    return conn, cursor

def view_db_by_level_all(cursor, view_db_config, viewing_type, category_list):
    # Assign local vars and count entries applicable to current viewing_type
    search_values = view_db_config[viewing_type]['search_value']
    query = view_db_config[viewing_type]['query']
    category_list = view_db_config[viewing_type]['category_list']
    count = view_table_count_query_builder(cursor, query)

    # Display list of chosen categories in order: clothing type (e.g. tops), sub-type (e.g. crops), individual pieces by brand name (e.g. monki)
    res_list = db_viewer_message(viewing_type, category_list, search_values, count)
    
    # Request user choice and check if exists as a category
    chosen_category = input("> ")
    if chosen_category not in res_list:
        raise ValueError(f"{ERR_INVALID_INPUT}: '{chosen_category}'")
    view_db_config[viewing_type]['chosen_category'] = chosen_category

    return chosen_category

def view_db_by_level_spec(cursor, view_db_config, viewing_type):
    chosen_category = view_db_config[viewing_type]['chosen_category']
    if viewing_type == 'clothing type':
        category_list = clothing_type_to_sub_dict[chosen_category]
        next_query = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % ','.join("'{}'".format(value) for value in category_list)
        
    elif viewing_type == 'clothing sub-type':
        category_list_query = VIEW_CLOTHING_ENTRIES + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{chosen_category}'"
        try:
            cursor.execute(category_list_query)
        except psycopg2.Error as e:
            raise Exception(f"{ERR_DB_QUERY}: {e}")
        category_list = cursor.fetchall()
        next_query = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{chosen_category}'"

    return category_list, next_query

def view_table_count_query_builder(cursor, query):
    try:
        cursor.execute(query)
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_QUERY}: {e}")
    count = cursor.fetchone()[0]
    return count

def db_viewer_message(category, category_list, search_values, count):
    if category == 'individual piece':
        items = [item[1] for item in category_list]
        sorted_items = sorted(items)
    else:
        sorted_items = category_list

    res_list = '\n'.join(sorted_items)
    print(MSG_DB_VIEWER.format(category, res_list, f"'{search_values}'", count))
    return sorted_items

def query_to_class_chosen_item(cursor, view_db_config):
    # Create and execute query based on final user choice
    individual_piece_name = view_db_config['clothing sub-type']['chosen_category']
    chosen_clothing_item_query = VIEW_CLOTHING_ENTRIES + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{individual_piece_name}'"
    
    try:
        cursor.execute(chosen_clothing_item_query)
    except psycopg2.Error as e:
        raise Exception(f"{ERR_DB_QUERY}: {e}")
    res = cursor.fetchone()

    # Convert data into Class object for neat display
    brand_name, type_name, thumbnail_path, date_bought, wear_count = res[1], res[2], res[3], res[4], res[5]
    date_removed = 'N/A' if res[6] is None else res[6]
    chosenClothingItem = ClothingEntry(brand_name, type_name, thumbnail_path, date_bought, wear_count, date_removed)
    return chosenClothingItem