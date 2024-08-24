# Handles view of entries and properties for clothing items
# User permissions: GRANT pg_read_server_files TO your_username;
import psycopg2
from constants.errors import *
from constants.messages import MSG_DB_VIEWER
from constants.db_commands import *
from objects.clothing import ClothingEntry

def view_db():
    # Initial db connection & cursor
    try:
        conn = psycopg2.connect(database="my_closet",
                                host="localhost",
                                user="choiwanyip",
                                password="",
                                port="5432")
    except:
        print(ERR_DB_CONN)
        return 1

    cursor = conn.cursor()

    # Setup db tables from scratch
    for query in [RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES]:
        cursor.execute(query)

    # Options presented to user
    view_db_config = {
        'clothing type': {
            'query': VIEW_TABLE_COUNT,
            'search_value': 'all',
        },
        'clothing sub-type': {}, 
        'individual piece': {}
    }
    clothing_type_to_sub_dict = {
        'tops':['crop','flannel','jumper','sheer','shirt','sleeveless'],
        'bottoms':['culottes','jeans','jeggings','shorts','skort','trousers'],
        'dresses':['skater','midi','maxi'],
        'jackets':['bomber','coat','fleece','hoodie','denim','sherpa','windbreaker']
    }

    view_db_config['clothing type']['category_list'] = clothing_type_to_sub_dict.keys()
    keys_list = list(view_db_config.keys())
    for i, viewing_type in enumerate(view_db_config.keys()):
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
            print(ERR_INVALID_INPUT)
            return 1
        view_db_config[viewing_type]['chosen_category'] = chosen_category
        
        # Create query for next viewing type 
        if i < 2:
            next_key = keys_list[i+1]

            if i == 0: # Clothing type chosen, moving onto sub-types
                category_list = clothing_type_to_sub_dict[chosen_category]
                next_query = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % ','.join("'{}'".format(value) for value in category_list)

            if i == 1: # Clothing sub-type chosen, moving onto individual pieces' brand names                
                category_list_query = VIEW_CLOTHING_ENTRIES + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{chosen_category}'"
                cursor.execute(category_list_query)
                category_list = cursor.fetchall()
                next_query = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{chosen_category}'"
            
            view_db_config[next_key]['query'] = next_query
            view_db_config[next_key]['search_value'] = chosen_category
            view_db_config[next_key]['category_list'] = category_list

        else: break

    # Query & collate data on chosen clothing item
    individual_piece_name = view_db_config['clothing sub-type']['chosen_category']
    chosen_clothing_item_query = VIEW_CLOTHING_ENTRIES + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{individual_piece_name}'"
    cursor.execute(chosen_clothing_item_query)
    res = cursor.fetchone()
    brand_name, type_name, thumbnail_path, date_bought, wear_count = res[1], res[2], res[3], res[4], res[5]
    date_removed = 'N/A' if res[6] is None else res[6]
    chosenClothingItem = ClothingEntry(brand_name, type_name, thumbnail_path, date_bought, wear_count, date_removed)
    print(chosenClothingItem)    

    conn.close()
    return 0

def view_table_count_query_builder(cursor, query):
    cursor.execute(query)
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