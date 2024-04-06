from constants.messages import *
from modules.add_new import add_new
from modules.view_db import view_db

# Landing page - user to select whether to add or view clothes
action_item = input(MSG_GREET)

match action_item:
    case "a":
        # functionality of modules/add_new
        add_new()
    case "b":
        # functionality of modules/view_clothes
        view_db()
    case _:
        print("Error in input. Closing...\n")

