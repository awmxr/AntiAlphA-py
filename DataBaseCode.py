from os import pathsep

import sqlite3
import datetime as dt


List01 = ["sha1" , "sha256" , "md5",
"Bkav",
"Lionic",
"ClamAV",
"CMC",
"CAT_QuickHeal",
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
"ESET_NOD32",
"TrendMicro_HouseCall",
"Avast",
"Cynet",
"Kaspersky",
"BitDefender",
"NANO_Antivirus",
"ViRobot",
"MicroWorld_eScan",
"Rising",
"Emsisoft",
"Baidu",
"F_Secure",
"DrWeb",
"Zillya",
"TrendMicro",
"McAfee_GW_Edition",
"FireEye",
"Sophos",
"Ikarus",
"Jiangmin",
"Avira",
"Antiy_AVL",
"Kingsoft",
"Gridinsoft",
"Xcitium",
"Microsoft",
"SUPERAntiSpyware",
"ZoneAlarm",
"GData",
"Google",
"AhnLab_V3",
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
def Create_Database():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE Request (
        Id integer PRIMARY KEY,
        FileName text,
        Size text,
        Resource text,
        State integer,
        Time text,
        Sha256 text
        
        )""")

    c.execute("""CREATE TABLE Max (
        Id integer,
        Size integer
        
        )""")


    c.execute("""CREATE TABLE Response (
        Id integer PRIMARY KEY,
        ReqId integer,
        Time text,
        sha1 text,
        sha256 text,
        md5 text,
        Bkav integer,
        Lionic integer,
        ClamAV integer,
        CMC integer,
        CAT_QuickHeal integer,
        McAfee integer,
        Malwarebytes integer,
        VIPRE integer,
        Sangfor integer,
        K7AntiVirus integer,
        K7GW integer,
        Arcabit integer,
        BitDefenderTheta integer,
        VirIT integer,
        Cyren integer,
        Symantec integer,
        ESET_NOD32 integer,
        TrendMicro_HouseCall integer,
        Avast integer,
        Cynet integer,
        Kaspersky integer,
        BitDefender integer,
        NANO_Antivirus integer,
        ViRobot integer,
        MicroWorld_eScan integer,
        Rising integer,
        Emsisoft integer,
        Baidu integer,
        F_Secure integer,
        DrWeb integer,
        Zillya integer,
        TrendMicro integer,
        McAfee_GW_Edition integer,
        FireEye integer,
        Sophos integer,
        Ikarus integer,
        Jiangmin integer,
        Avira integer,
        Antiy_AVL integer,
        Kingsoft integer,
        Gridinsoft integer,
        Xcitium integer,
        Microsoft integer,
        SUPERAntiSpyware integer,
        ZoneAlarm integer,
        GData integer,
        Google integer,
        AhnLab_V3 integer,
        Acronis integer,
        ALYac integer,
        TACHYON integer,
        VBA32 integer,
        Zoner integer,
        Tencent integer,
        Yandex integer,
        MAX integer,
        MaxSecure integer,
        Fortinet integer,
        AVG integer,
        Panda integer
        
        
        )""")

    c.execute("""CREATE TABLE Request_URL (
        Id integer PRIMARY KEY,
        URL text,
        Resource text,
        State integer,
        Time text
        
        )""")

    c.execute("""CREATE TABLE Response_URL (
        Id integer PRIMARY KEY,
        ReqId integer,
        Time text,
        Secure integer
        
        
        )""")
    with conn:
        c.execute("INSERT INTO Max VALUES (:Id ,:Size)", {
                        'Id':1, 'Size' : 33554432})
    conn.close()



def get_all_Request_URL():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT URL FROM Request_URL")
    b = c.fetchall()
    conn.close()
    
    final_list = []
    for i in b:
        final_list.append(i[0])
    # print(final_list)
    return final_list

# get_all_Request_URL()

def get_scaned_URLs():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    with conn:
        c.execute(f"SELECT Id, Url FROM Request_URL WHERE State = :State",{'State':1})
    b = c.fetchall()
    # print(b)

    v = []
    f = []
    for i in b:
        v.append(i[0])
        f.append(i[1])
    # print(v)
    final_list = []
    

    for i in range(len(v)):
        with conn:
            c.execute(f"SELECT * FROM Response_URL WHERE ReqId = :ReqId",{'ReqId':v[i]})
        n = list(c.fetchone())

        n.append(f[i])
        final_list.append(n)


    conn.close()
    
    return final_list

def Update_State_URL(Id):
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()    
    with conn:
        
        c.execute("""UPDATE Request_URL SET State = :State WHERE Id = :Id""",{'Id':Id, 'State':1})
    conn.close()

def get_last_Response_URL():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM Response_URL ORDER BY Id DESC LIMIT 1")
    b = c.fetchone()
    conn.close()
    if b:
        return int(b[0]) + 1
    else:
        return 1

def insert_Response_URL(ReqId , Time , Secure):
    id = get_last_Response_URL()
    string_res_insert = insert_string_response()
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    try:
        with conn:
            c.execute(f"INSERT INTO Response_URL VALUES (:Id ,:ReqId ,:Time ,:Secure)", {
                    'Id' : id, 'ReqId' : ReqId , 'Time': Time , 'Secure' : Secure})
        conn.close()
        return True
    except:
        conn.close()
        return False
    


def get_last_Request_URL():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM Request_URL ORDER BY Id DESC LIMIT 1")
    b = c.fetchone()
    conn.close()
    if b:
        return int(b[0]) + 1
    else:
        return 1

def insert_Request_URL(URL , Resource , State , Time ):
    # print(Sha256)
    id = get_last_Request_URL()
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    c.execute(f"SELECT * FROM Request_URL WHERE URL = :URL",{'URL':URL})
    b = c.fetchone()
    # conn.close()
    if b != None:
        return 3
        
    else:
        

        try:
            with conn:
                c.execute("INSERT INTO Request_URL VALUES (:Id ,:URL ,:Resource, :State, :Time)", {
                        'Id' : id, 'URL' : URL , 'Resource': Resource, 'State' : State ,'Time' : Time})
            conn.close()
            return True
        except:
            conn.close()
            return False



def get_not_scaned_Urls():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    with conn:
        c.execute(f"SELECT * FROM Request_URL WHERE state = :state",{'state':0})
    b = c.fetchall()
    conn.close()
    # print(b)
    return b 



def Update_Size_max(newsize):
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()    
    with conn:
        
        c.execute("""UPDATE Max SET Size = :Size WHERE Id = :Id""",{'Id':1, 'Size':newsize})
    conn.close()

def get_max_size():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM Max ORDER BY Id DESC LIMIT 1")
    b = c.fetchone()
    conn.close()
    if b:
        return int(b[1])
    else:
        return -1

def get_last_Request():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM Request ORDER BY Id DESC LIMIT 1")
    b = c.fetchone()
    conn.close()
    if b:
        return int(b[0]) + 1
    else:
        return 1

def insert_Request(FileName , Size , Resource ,State, Time , Sha256):
    # print(Sha256)
    id = get_last_Request()
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    c.execute(f"SELECT * FROM Request WHERE Sha256 = :Sha256",{'Sha256':Sha256})
    b = c.fetchone()
    # conn.close()
    if b != None:
        return 3
        
    else:
        

        try:
            with conn:
                c.execute("INSERT INTO Request VALUES (:Id ,:FileName ,:Size, :Resource, :State, :Time, :Sha256)", {
                        'Id' : id, 'FileName' : FileName , 'Size': Size, 'Resource' : Resource ,'State' : State, 'Time' : Time , 'Sha256':Sha256})
            conn.close()
            return True
        except:
            conn.close()
            return False



def get_last_Response():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM Response ORDER BY Id DESC LIMIT 1")
    b = c.fetchone()
    conn.close()
    if b:
        return int(b[0]) + 1
    else:
        return 1

def insert_Response(ReqId , Time , List02):
    id = get_last_Response()
    string_res_insert = insert_string_response()
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    try:
        with conn:
            c.execute(f"INSERT INTO Response VALUES (:Id ,:ReqId ,:Time{string_res_insert})", {
                    'Id' : id, 'ReqId' : ReqId , 'Time': Time , List01[0]:List02[0],List01[1]:List02[1],List01[2]:List02[2],List01[3]:List02[3],List01[4]:List02[4],List01[5]:List02[5],List01[6]:List02[6],List01[7]:List02[7],List01[8]:List02[8],List01[9]:List02[9],List01[10]:List02[10],List01[11]:List02[11],List01[12]:List02[12],List01[13]:List02[13],List01[14]:List02[14],List01[15]:List02[15],List01[16]:List02[16],List01[17]:List02[17],List01[18]:List02[18],List01[19]:List02[19],List01[20]:List02[20],List01[21]:List02[21],List01[22]:List02[22],List01[23]:List02[23],List01[24]:List02[24],List01[25]:List02[25],List01[26]:List02[26],List01[27]:List02[27],List01[28]:List02[28],List01[29]:List02[29],List01[30]:List02[30],List01[31]:List02[31],List01[32]:List02[32],List01[33]:List02[33],List01[34]:List02[34],List01[35]:List02[35],List01[36]:List02[36],List01[37]:List02[37],List01[38]:List02[38],List01[39]:List02[39],List01[40]:List02[40],List01[41]:List02[41],List01[42]:List02[42],List01[43]:List02[43],List01[44]:List02[44],List01[45]:List02[45],List01[46]:List02[46],List01[47]:List02[47],List01[48]:List02[48],List01[49]:List02[49],List01[50]:List02[50],List01[51]:List02[51],List01[52]:List02[52],List01[53]:List02[53],List01[54]:List02[54],List01[55]:List02[55],List01[56]:List02[56],List01[57]:List02[57],List01[58]:List02[58],List01[59]:List02[59],List01[60]:List02[60],List01[61]:List02[61],List01[62]:List02[62]})
        conn.close()
        return True
    except:
        conn.close()
        return False
    
        


def get_not_scaned_files():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    with conn:
        c.execute(f"SELECT * FROM Request WHERE state = :state",{'state':0})
    b = c.fetchall()
    conn.close()
    # print(b)
    return b 



def insert_string_response():
    string1 = ""
    for i in List01:
        string1 += f" ,:{i}"
    
    
    return string1


def Update_State(Id):
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()    
    with conn:
        
        c.execute("""UPDATE Request SET State = :State WHERE Id = :Id""",{'Id':Id, 'State':1})
    conn.close()



def get_scaned_files():
    conn = sqlite3.connect('Nava.db')
    c = conn.cursor()
    
    with conn:
        c.execute(f"SELECT Id, FileName FROM Request WHERE State = :State",{'State':1})
    b = c.fetchall()
    # print(b)

    v = []
    f = []
    for i in b:
        v.append(i[0])
        f.append(i[1])
    # print(v)
    final_list = []
    

    for i in range(len(v)):
        with conn:
            c.execute(f"SELECT * FROM Response WHERE ReqId = :ReqId",{'ReqId':v[i]})
        n = list(c.fetchone())

        n.append(f[i])
        final_list.append(n)


    conn.close()
    
    return final_list
