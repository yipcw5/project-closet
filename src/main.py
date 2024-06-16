from constants.messages import *
from constants.errors import ERR_INVALID_INPUT
from modules.add_new import add_new
from modules.view_db import view_db, refresh_db

def main():

    # init inventory
    df = refresh_db()

    # Landing page - user to select whether to add or view clothes
    action_item = input(MSG_GREET)

    match action_item:
        case "a":
            # functionality of modules/add_new
            return add_new(df)
        case "b":
            # functionality of modules/view_db
            return view_db(df)
        case _:
            print(ERR_INVALID_INPUT)
            return 1

if __name__ == "__main__":
    main()