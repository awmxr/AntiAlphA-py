from check_USB import check_usb
from check_path import check_drivers
from Scan import scan_file
from time import sleep
def Scan_Usb(myapikey):
    while True:
        if check_usb() == False:
            # print("x")
            sleep(5)
        else:
            print("\n\tusb recognized!")
            
            list_of_dir_usb = check_drivers()
            list_of_dir_usb2 = list_of_dir_usb
            # print(list_of_dir_usb)
            for i in list_of_dir_usb:
                print("\nFile Directory : " ,i)
                scan_file(myapikey,i)
            while list_of_dir_usb == list_of_dir_usb2:
                list_of_dir_usb2 = check_drivers()
                sleep(5)


            


