from const import *

ans_option = input(msg_greet)

def read_file(file_name):
    file_handle = open(file_name)
    print(file_handle.read())
    file_handle.close()

match ans_option:
    case "a":
        img_path = input(msg_enter_img_path)
        read_file(img_path)
    case "b":
        print(clothes_list)
    case _:
        print("Error in input. Closing...\n")
        
