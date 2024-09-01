'''
Add new item of clothing
'''

from constants.errors import ERR_INVALID_INPUT
from constants.messages import MSG_ADD_NEW_OPTIONS

def add_new_main():
    '''Landing page for available options'''
    add_new_action = input(MSG_ADD_NEW_OPTIONS)
    match add_new_action:
        case '1':
            pass
        case '2':
            pass
        case _:
            raise ValueError(f"{ERR_INVALID_INPUT}: '{add_new_action}'")
