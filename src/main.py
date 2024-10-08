from constants.messages import MSG_GREET, MSG_PROGRAM_COMPLETE
from constants.errors import ERR_INVALID_INPUT
from modules.add_new.add_new import add_new_main
from modules.view_db.view_db import view_db_main
from modules.helper.db_helper import init_db

def main():

    conn = init_db()

    # Landing page - user to select whether to add or view clothes
    action_item = input(MSG_GREET)

    match action_item:
        case "a":
            # functionality of modules/add_new
            add_new_main(conn)
        case "b":
            # functionality of modules/view_db
            view_db_main(conn)
        case _:
            raise ValueError(f"{ERR_INVALID_INPUT}: '{action_item}'")
    
    print(MSG_PROGRAM_COMPLETE)
    conn.close()

if __name__ == "__main__":
    main()