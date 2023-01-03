# oooo     oooo      o      ooooo  oooo   ooooooo   ooooooooooo ooooooooooo 
# 8888o   888      888       888  88   o88     888 88  888  88 88    888   
# 88 888o8 88     8  88        888           o888      888         888     
# 88  888  88    8oooo88      88 888      o888   o     888       888    oo 
# o88o  8  o88o o88o  o888o o88o  o888o o8888oooo88    o888o    o888oooo888                                                                         
# link  https://github.com/max2tz/Authentication
# author  max2tz https://github.com/max2tz
# license  GPL-3.0 License 


import subprocess
import requests

def get_hardware_id():
    hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return hardwareid

def check_hwid():
    hwid = get_hardware_id()
    auth = requests.post("http://your-server.server/check_hwid", json={"hwid": hwid})
    if auth.status_code == 200: # Successful - HWID Is Valid
        return True
    elif auth.status_code == 401: # Unuccessful - HWID Is Invalid
        return False

if check_hwid():
    print('Your Code For When There HWID Is Valid') # If Check_HWID Returned True
else:
    print('Your Code For When There HWID Is Invalid') # If Check_HWID Returned False

