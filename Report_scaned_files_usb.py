import requests
from DataBaseCode import insert_Response , get_scaned_files ,Update_State
import datetime as dt
from time import sleep

def get_report_scaned_files_usb():
    
    scaned_files = get_scaned_files()
    if len(scaned_files) == 0:
        print("no usb report")
    else:
        for record in scaned_files:
            print(f"\nFile Directory : {record[-1]}")
            # print(f"\tsha1 : {record[3]}")
            # print(f"\tsha256 :{record[4]}")
            # print(f"\tmd5 : {record[5]}")
            print(f"\tscaned at : {record[2]}")
            secure = 1
            for i in range(6 , len(record) - 1):
                
                if record[i] == 1:
                    secure = 0
                
            if secure == 0:
                print("\n\t\tfile is not secure")

            if secure == 1:
                print("\n\t\tfile is secure")
            

            
            print("\t - - - - - - - - -")

                



    # print("done")


# get_report_scaned_files()