# import requests
import os
from threading import Thread
from Scan import scan_file
from Report_not_scaned_files import get_report_not_scaned_files
from Report_scaned_files import get_report_scaned_files
from Report_scaned_files_usb import get_report_scaned_files_usb 
from Report_scaned_Urls import get_report_scaned_URLs
from Scan_Usb import Scan_Usb
import datetime as dt
from time import sleep
from DataBaseCode import get_max_size , Update_Size_max , Create_Database , get_not_scaned_files, get_not_scaned_Urls
from Check_Chrome import check_Chrome
from Report_not_scaned_URLs import get_report_not_scaned_urls



my_api = "0fd6ffc9b80a535c07ced51d92255614b7663a95f48153840bf3041653f8caa2"


while True:
    if os.path.isfile("D:/Amir/UMZ/Hozuri/07/Sec/project/nava/Nava.db") == False:
        print("creating Database (Nava.db) . . .")
        Create_Database()
        sleep(2)
    os.system("cls")

        
    thread01 = Thread(target = Scan_Usb, args = (my_api, ))
    thread02 = Thread(target = get_report_not_scaned_files, args = (my_api, ))
    thread03 = Thread(target = check_Chrome, args = (my_api, ))
    thread04 = Thread(target = get_report_not_scaned_urls, args = (my_api, ))

    
    thread02.start()
    print("start to get report for not scaned file ...")
    thread01.start()
    print("start to check usb diroctory ...")
    thread03.start()
    print("start to check google chrome ...")
    thread04.start()
    print("start to get report for not scaned urls ...")
    sleep(10)
    # exit(0)
    os.system("cls")
    while True:
        maximum_Size = get_max_size()
        print("\n")
        print(f"maximum Size : {maximum_Size}Byte")
        print("\tMenu")
        print("- - - - - - - - - - - - ")
        print("1.show report files scan")        
        print("2.change maximum Size")
        print("3.show files in scan queue")
        print("4.show report Urls scan")
        print("5.show urls in scan queue")
        print("0.clear terminal")
        print("\n\n\n")
        

        try:
            inputuser = int(input("\tchoose : "))
        except:
            print("please just enter a integer")
            continue
        os.system("cls")
        if inputuser == 1:

            get_report_scaned_files_usb()
        elif inputuser == 2:
            while True:
                try:
                    inputuser2 = int(input("\Please Enter a integer between 1000 and  33554432 : "))
                except:
                    print("please just enter a integer bigger than 1000 and smaller than 33554432B")
                    continue

                if inputuser2 < 1000 :
                    print("input must bigger than 1000B")
                    continue
                elif inputuser2 > 33554432:
                    print("input must Smaller than 33554432B")
                    continue
                
                Update_Size_max(inputuser2)

                print(f"maximum size from {maximum_Size} updated to {inputuser2}")
                break

        elif inputuser == 3:
            not_scaned_files = get_not_scaned_files()
            final_string = "\n"
            i = 0
            for record in not_scaned_files:
                i+=1
                final_string += f"\n\t{i}. FileDirectory : {record[1]}\n\tRequest Time : {record[6]}\n\tSize : {record[2]}\n\tsha256 : {record[7]}\n\t Resource : {record[3]}\n"
                final_string += "\t- - - - - - - - - - - - - - - - - - - - - - - - - - - "
            
            print(final_string)
            sleep(10)

                
        elif inputuser == 4:

            get_report_scaned_URLs()

        elif inputuser == 5:
            not_scaned_urls = get_not_scaned_Urls()
            final_string = "\n"
            i = 0
            for record in not_scaned_urls:
                i+=1
                final_string += f"\n\t{i}. URL : {record[1]}\n\tRequest Time : {record[4]}\n\tSize : {record[2]}\n\t Resource : {record[2]}\n"
                final_string += "\t- - - - - - - - - - - - - - - - - - - - - - - - - - - "
            
            print(final_string)
            sleep(10)
        elif inputuser == 0:
            os.system("cls")
        else:
            print("please just enter a integer")
        






