import os


def check_drivers():

    drive_lists = ["A","B","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    final_list = []
    for i in drive_lists:

        res = os.path.isdir(f'{i}:')
        if res == True:
            x = f"{i}:/"
            listdir = os.listdir(f"{i}:")
            for j in listdir:
                if "s0" in j:
                    continue
                if "S0" in j:
                    continue
                x+= j
                # print(x)
                final_list.append(x)
                x = f"{i}:/"
                

            
    # print(final_list)
    return final_list



check_drivers()