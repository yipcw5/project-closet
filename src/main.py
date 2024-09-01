from constants.messages import MSG_GREET
from constants.errors import ERR_INVALID_INPUT
from modules.add_new.add_new import add_new_main
from modules.view_db.view_db import view_db_main

def main():

    # Landing page - user to select whether to add or view clothes
    action_item = input(MSG_GREET)

    match action_item:
        case "a":
            # functionality of modules/add_new
            return add_new_main()
        case "b":
            # functionality of modules/view_db
            return view_db_main()
        case _:
            raise ValueError(f"{ERR_INVALID_INPUT}: '{action_item}'")

if __name__ == "__main__":
    main()