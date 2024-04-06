# Add new item of clothing

from const import msg_enter_img_path

def add_new():
    img_path = input(msg_enter_img_path)
    read_file(img_path)

def read_file(file_name):
    file_handle = open(file_name)
    print(file_handle.read())
    file_handle.close()