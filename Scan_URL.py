import requests
import os
import datetime as dt
from DataBaseCode import insert_Request_URL
from time import sleep


def scan_URL(myapikey , URL ):        
    SCAN_URL = 'https://www.virustotal.com/vtapi/v2/url/scan'

    params = {'apikey': myapikey, 'url':URL}


    
    # print("x1")
    while True:
        try:
            response = requests.post(SCAN_URL,params=params)
            
            # sleep(4)
            res = response.json()
            break
        except requests.exceptions.ConnectionError:
            print("\t\tconnection error")
            pass
        except:
            if res.status_code == 204:
                print("too many request")
                print("sleep 10 sec")
                sleep(10)
    
    # print("x2")
    # print(response.json())
    # print(os.path.getsize(file))
    
    # print("x3")
    try:
        result = insert_Request_URL(URL, res["resource"],0,dt.datetime.now())
    except:
        return
    # print("x4")
    if result == 3:
        print("\t\tthis URL is already scaned")
    # print(result)
    elif result == True:
        
        print(f"\t scan Request for {URL} sent to virustotal server!")
    # print("x6")
    # print(result)


    #  insert request

