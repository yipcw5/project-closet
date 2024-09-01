# Config of options presented to user

from constants.db_commands.view_by_entry import VIEW_TABLE_COUNT

view_db_config_template = {
    'clothing type': {
        'query': VIEW_TABLE_COUNT,
        'search_value': 'all',
    },
    'clothing sub-type': {'query': '', 'search_value': ''}, 
    'individual piece': {'query': '', 'search_value': ''}
}

clothing_type_to_sub_dict = {
    'tops':['crop','flannel','jumper','sheer','shirt','sleeveless'],
    'bottoms':['culottes','jeans','jeggings','shorts','skort','trousers'],
    'dresses':['skater','midi','maxi'],
    'jackets':['bomber','coat','fleece','hoodie','denim','sherpa','windbreaker']
}