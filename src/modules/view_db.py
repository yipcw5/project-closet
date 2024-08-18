# Handles view of entries and properties for clothing items
# User permissions: GRANT pg_read_server_files TO your_username;
import psycopg2
from constants.errors import *
from constants.messages import MSG_DB_VIEWER
from constants.db_commands import *

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

    cursor = conn.cursor()

    # Setup db tables from scratch

    cursor.execute(RESET_DB)
    cursor.execute(INIT_TABLES)
    cursor.execute(INIT_FROM_CSV)
    cursor.execute(VIEW_CLOTHING_ENTRIES)

    # Options presented to user

    view_db_order = ['clothing type', 'clothing sub-type', 'individual piece']
    clothing_type_to_sub_dict = {
        'tops':['crop','flannel','jumper','sheer','shirt','sleeveless'],
        'bottoms':['culottes','jeans','jeggings','shorts','skort','trousers'],
        'dresses':['skater','midi','maxi'],
        'jackets':['bomber','coat','fleece','hoodie','denim','sherpa','windbreaker']
    }

    # View: clothing type
    cursor.execute(VIEW_TABLE_COUNT)
    count = cursor.fetchone()[0]
    db_viewer_message(view_db_order[0], clothing_type_to_sub_dict.keys(),count)

    clothing_type_to_sub_key = input("> ")
    if clothing_type_to_sub_key not in clothing_type_to_sub_dict.keys(): print(ERR_INVALID_INPUT)

    # View: clothing sub-type
    clothing_type_to_sub_values = clothing_type_to_sub_dict[clothing_type_to_sub_key]
    message = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % ','.join(['%s']*len(clothing_type_to_sub_values))
    cursor.execute(message, clothing_type_to_sub_values)
    count = cursor.fetchone()[0]
    db_viewer_message(view_db_order[1], clothing_type_to_sub_values, count)

    individual_piece_name = input("> ")
    if individual_piece_name not in clothing_type_to_sub_values: print(ERR_INVALID_INPUT)

    # View: individual piece
    message = VIEW_CLOTHING_ENTRIES + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{individual_piece_name}'"
    cursor.execute(message)
    category_list = cursor.fetchall()
    count_query = VIEW_TABLE_COUNT + VIEW_CLOTHING_ENTRIES_BY_SUBTYPE % f"'{individual_piece_name}'"
    cursor.execute(count_query, individual_piece_name)
    count = cursor.fetchone()[0]
    db_viewer_message(view_db_order[2], category_list, count)

    conn.close()

def db_viewer_message(category, category_list, count):
    if category == 'clothing type' or category == 'clothing sub-type':
        res_list = '\n'.join(category_list)

    else:
        items = [item[1] for item in category_list]
        sorted_items = sorted(items)
        res_list = '\n'.join(sorted_items)

    print(MSG_DB_VIEWER.format(category, res_list, count))
    