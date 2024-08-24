# Add new item of clothing

import os
import csv

from constants.errors import ERR_INVALID_INPUT
from constants.messages import MSG_ENTER_CLOTHING_TYPE
from objects.clothing import ClothingItem
from modules.view_db import refresh_db

DB_PATH = "src/databases/clothing_inventory.csv"

# Check file exists and fill in clothing item details
def add_new(df):

    ## User entry for new clothing item entry
    clothing_brand = input("Enter clothing brand: ")
    clothing_colour = input("Enter clothing colour: ")

    ## Extract clothing types that exist, to be printed
    clothing_types_existing = df['clothing_type']
    clothing_types_set = set(clothing_types_existing.tolist())
    clothing_type = input(MSG_ENTER_CLOTHING_TYPE.format(clothing_types_set))

    filename = input("Enter filename. Ensure this exists under ./thumbnails. ")
    if os.path.isfile("./thumbnails/" + filename) == False:
        print(ERR_INVALID_INPUT)
        add_new(df)

    ## Print new clothing item entry
    newClothingItem = ClothingItem(clothing_brand, clothing_colour, clothing_type, filename)

    print("Confirm entry [y or otherwise]:\n", newClothingItem)
    confirm_answer = input()
    match confirm_answer:
        case "y":
            # Update CSV (dataframe excluded)
            row_values = [len(df), clothing_brand, clothing_colour, clothing_type, filename, 0]

            with open(DB_PATH, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                row_keys = reader.fieldnames

            with open(DB_PATH, mode='a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=row_keys)
                
                new_row = {key: value for key, value in zip(row_keys, row_values)}

                # Write the new row
                writer.writerow(new_row)
                clothing_id = len(df) + 2

            print("Entry successful and added to inventory with ID:", clothing_id)
            df = refresh_db()
        case _:
            print("Trying again...\n\n")
            add_new()
    return df