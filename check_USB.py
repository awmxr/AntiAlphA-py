import os


def check_usb():
    drive_lists = ["A","B","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    
    for i in drive_lists:

        res = os.path.isdir(f'{i}:')
        if res == True:
            return True
        
    return False
# print(check_usb())