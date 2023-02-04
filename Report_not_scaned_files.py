import requests
from DataBaseCode import insert_Response , get_not_scaned_files ,Update_State
import datetime as dt
from time import sleep

def get_report_not_scaned_files(myapikey):
    while True:
        not_scaned_files = get_not_scaned_files()
        for record in not_scaned_files:
            
            
            time_delay = dt.datetime.fromisoformat(record[5])
            # print(time_delay)
            if dt.datetime.now() - time_delay < dt.timedelta(seconds=120):
                # print(f"{record[1]} :")
                
                # print("\t\tat least take 2 min")
                continue
            

            # time_delay = dt.datetime(record[6])
            # print(time_delay)
            
            REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': myapikey, 'resource': record[3]}
            res = None
            while True:
                try:
                    resT = requests.get(REPORT_URL, params=params)
                    res = resT
                    break
                except requests.exceptions.ConnectionError:
                    # print("connection error\ntry to connect")
                    pass

            res = res.json()
            if "queued" in res["verbose_msg"]:
                # print(f"{record[1]} :")
                # print("\t\tnot scaned by virussotal server yet")
                continue
            List01 = ["sha1" , "sha256" , "md5",
            "Bkav",
            "Lionic",
            "ClamAV",
            "CMC",
            "CAT-QuickHeal",
            "McAfee",
            "Malwarebytes",
            "VIPRE",
            "Sangfor",
            "K7AntiVirus",
            "K7GW",
            "Arcabit",
            "BitDefenderTheta",
            "VirIT",
            "Cyren",
            "Symantec",
            "ESET-NOD32",
            "TrendMicro-HouseCall",
            "Avast",
            "Cynet",
            "Kaspersky",
            "BitDefender",
            "NANO-Antivirus",
            "ViRobot",
            "MicroWorld-eScan",
            "Rising",
            "Emsisoft",
            "Baidu",
            "F-Secure",
            "DrWeb",
            "Zillya",
            "TrendMicro",
            "McAfee-GW-Edition",
            "FireEye",
            "Sophos",
            "Ikarus",
            "Jiangmin",
            "Avira",
            "Antiy-AVL",
            "Kingsoft",
            "Gridinsoft",
            "Xcitium",
            "Microsoft",
            "SUPERAntiSpyware",
            "ZoneAlarm",
            "GData",
            "Google",
            "AhnLab-V3",
            "Acronis",
            "ALYac",
            "TACHYON",
            "VBA32",
            "Zoner",
            "Tencent",
            "Yandex",
            "MAX",
            "MaxSecure",
            "Fortinet",
            "AVG",
            "Panda"]
            
            # print("\n")
            final_list = []
            final_list.append(res["sha1"])
            final_list.append(res["sha256"])
            final_list.append(res["md5"])
            for i in range (3,63):
                # print(i)
                
                # print(res["scans"][List01[i]]["detected"])
                x = 1
                try:
                    if res["scans"][List01[i]]["detected"] == False:
                        x = 0
                except:
                    x = 0
                

                # if x == 1:
                #     print(List01[i],end=" : ")
                #     print("the file is not secure!")
                final_list.append(x)


            result = insert_Response(record[0] , str(dt.datetime.now()) , final_list)
            if result == True:
                Update_State(record[0])

            print(f"\tfile {record[1]} scans complited")
            # print(res["sha1"])
            # print(res["sha256"])
            # print(res["md5"])

            # print(res.json())

            # print(result)
        sleep(120)
    # print("done")

my_api = "0fd6ffc9b80a535c07ced51d92255614b7663a95f48153840bf3041653f8caa2"
# get_report_not_scaned_files( my_api)