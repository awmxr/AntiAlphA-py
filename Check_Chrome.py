import pywinauto
from extraxt_domain import extraxt_domain
from Scan_URL import scan_URL
from time import sleep
from DataBaseCode import get_all_Request_URL
def check_Chrome(mykeyapi):
    while True :

        allurlrequested = get_all_Request_URL()
        
        try:
        
            desktop = pywinauto.Desktop(backend="uia")
            window = desktop.windows(title_re=".* Google Chrome$", control_type="Pane")[0]
            wrapper_list = window.descendants(control_type="TabItem")
            wrapper_url = window.descendants(title="Address and search bar", control_type="Edit")[0]
            # for wrapper in wrapper_list:
                # wrapper.click_input()
                
            x = wrapper_url.get_value()
            domain = extraxt_domain(x)
            if not domain in allurlrequested:
                scan_URL(mykeyapi,domain)
                print(domain)
            sleep(3)
        except IndexError:

            pass
# check_Chrome("sas")