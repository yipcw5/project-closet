# Add new item of clothing

import os

from constants.messages import msg_enter_img_path, msg_enter_clothing_details
from objects.clothing import ClothingItem

def add_new():
    img_path = input(msg_enter_img_path)

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
    clothing_type = input(msg_enter_clothing_details.format(cur_types))
    if clothing_type not in cur_types:
        print("ERROR: input not in possible values. Try again.")
        enter_clothing_type_details()