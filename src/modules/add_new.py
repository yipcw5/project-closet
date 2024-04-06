# Add new item of clothing

import os

from constants.messages import MSG_ENTER_IMG_PATH, MSG_ENTER_CLOTHING_DETAILS
from objects.clothing import ClothingItem

def add_new():
    img_path = input(MSG_ENTER_IMG_PATH)

    ## TESTING PURPOSES ONLY
    if img_path == 'test':
        img_path = '../thumbnails/coats/hollister-parka.webp'

    enter_details(img_path)

# Check file exists and fill in clothing item details
def enter_details(img_path):
    if os.path.isfile(img_path):
        clothing_brand = input("Enter clothing brand: ")
        clothing_colour = input("Enter clothing colour: ")
        clothing_type = enter_clothing_type_details()
        
        new_img_path = './thumbnails/' + clothing_type
        os.rename(img_path, new_img_path)

        newClothingItem = ClothingItem(clothing_brand, clothing_colour, clothing_type)

        print("Entry successful. Please confirm details are correct (y/n).\n", newClothingItem)
        answer = input("> ")
        if answer == 'n':
            enter_details(img_path)

def enter_clothing_type_details():
    cur_types = os.listdir('../thumbnails')
    clothing_type = input(MSG_ENTER_CLOTHING_DETAILS.format(cur_types))
    if clothing_type not in cur_types:
        print("ERROR: input not in possible values. Try again.")
        enter_clothing_type_details()