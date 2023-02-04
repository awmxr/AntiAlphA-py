import requests
import os
import datetime as dt
from DataBaseCode import insert_Request ,get_max_size
from time import sleep


def scan_file(myapikey , file ):
    maximum_Size = get_max_size()
    size_of_file = os.path.getsize(file)
    if maximum_Size < size_of_file:
        print(f"the maximum size is {maximum_Size} Byte but this file ({file})'s size is {size_of_file} Byte")
        print("\nafter 10 sec this message will be disappeared!")
        sleep(10)
        return
        

    SCAN_URL = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': myapikey}


    try:
        files = {'file': (file, open(file, 'rb'))}
    except PermissionError:
        print("\t\tPermissionError")
        return
    # print("x1")
    while True:
        try:
            response = requests.post(SCAN_URL, files=files, params=params)
            break
        except requests.exceptions.ConnectionError:
            print("\t\tconnection error")
            pass
    res = response.json()
    # print("x2")
    # print(response.json())
    # print(os.path.getsize(file))
    
    # print("x3")
    result = insert_Request(file , size_of_file , res["resource"],0,dt.datetime.now(),res["sha256"])
    # print("x4")
    if result == 3:
        print("\t\tthis file is already scaned")
    # print(result)
    elif result == True:
        print("x5")
        print(f"\t scan Request for {file} sent to virustotal server!")
    # print("x6")
    # print(result)


    #  insert request

