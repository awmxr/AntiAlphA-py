import requests
from DataBaseCode import insert_Response_URL , get_not_scaned_Urls ,Update_State_URL
import datetime as dt
from time import sleep

def get_report_not_scaned_urls(myapikey):
    while True:
        get_not_scaned_urls = get_not_scaned_Urls()
        for record in get_not_scaned_urls:
            
            
            time_delay = dt.datetime.fromisoformat(record[4])
            # print(time_delay)
            if dt.datetime.now() - time_delay < dt.timedelta(seconds=120):
                # print(f"{record[1]} :")
                
                print("\t\tat least take 2 min")
                continue
            

            # time_delay = dt.datetime(record[6])
            # print(time_delay)
            
            REPORT_URL = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = {'apikey': myapikey, 'resource': record[2]}
            res = None
            while True:
                try:
                    resT = requests.get(REPORT_URL, params=params)
                    res = resT
                    res = res.json()
                    break
                except requests.exceptions.ConnectionError:
                    # print("connection error\ntry to connect")
                    pass
                except:
                    if res.status_code == 204:
                        print("too many request")
                        print("sleep 10 sec")
                        sleep(10)

            
            if "queued" in res["verbose_msg"]:
                # print(f"{record[1]} :")
                # print("\t\tnot scaned by virussotal server yet")
                continue
           
            
            # print("\n")
            final_list = []
            keys = res['scans'].keys()
            Secure = 1
            for i in keys:
                if res['scans'][i]["detected"] == True:
                    Secure = 0
                    break
            



            result = insert_Response_URL(record[0] , str(dt.datetime.now()) ,Secure)
            if result == True:
                Update_State_URL(record[0])

            print(f"\tUrl {record[1]} scans complited")
            # print(res["sha1"])
            # print(res["sha256"])
            # print(res["md5"])

            # print(res.json())

            # print(result)
        sleep(120)
    # print("done")

my_api = "0fd6ffc9b80a535c07ced51d92255614b7663a95f48153840bf3041653f8caa2"
# get_report_not_scaned_files( my_api)