# Add new item of clothing

import os

from constants.errors import ERR_INVALID_INPUT
from constants.messages import MSG_ENTER_CLOTHING_DETAILS
from objects.clothing import ClothingItem

def add_new(img_path):

    ## TESTING PURPOSES ONLY
    if img_path == "t":
        img_path = '../thumbnails/coats/hollister-parka.webp'
    
    if os.path.isfile(img_path) == False:
        print(ERR_INVALID_INPUT)
        return 1

    enter_details(img_path)
    
    return 0

# Check file exists and fill in clothing item details
def enter_details(img_path):

        clothing_brand = input("Enter clothing brand: ")
        clothing_colour = input("Enter clothing colour: ")
        clothing_type, status = enter_clothing_type_details()
        if status == 1:
            return 1
        
        new_img_path = '../thumbnails/' + clothing_type + '/' + '-'.join([clothing_brand, clothing_colour, clothing_type]) + os.path.splitext(img_path)[-1]
        os.rename(img_path, new_img_path)

        newClothingItem = ClothingItem(clothing_brand, clothing_colour, clothing_type, new_img_path)

        print("Entry successful.\n", newClothingItem)

def enter_clothing_type_details():
    cur_types = os.listdir('../thumbnails')
    clothing_type = input(MSG_ENTER_CLOTHING_DETAILS.format(cur_types))
    status = 0
    if clothing_type not in cur_types:
        print(ERR_INVALID_INPUT)
        return clothing_type, 1
    return clothing_type, 0