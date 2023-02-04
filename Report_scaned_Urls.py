import requests
from DataBaseCode import insert_Response_URL , get_scaned_URLs ,Update_State_URL
import datetime as dt
from time import sleep

def get_report_scaned_URLs():
    
    scaned_Urls = get_scaned_URLs()
    if len(scaned_Urls) == 0:
        print("no url report")
    else:

        for record in scaned_Urls:
            print(f"\n{record[-1]}")
            print(f"\tscaned at : {record[2]}")
            secure = 1
            
                
            if record[3] == 1:
                secure = 1
                
            if int(secure) == 0:
                print("\n\t\tURL is not secure")

            if int(secure) == 1:
                print("\n\t\tURL is secure")
            

            
            print("\t - - - - - - - - - \n\n")

                



    # print("done")


