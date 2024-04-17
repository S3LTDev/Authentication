#  @@@@@@ @@@@@@  @@@      @@@@@@@      @@@@@@@  @@@@@@@@ @@@  @@@
# !@@         @@! @@!        @@!        @@!  @@@ @@!      @@!  @@@
#  !@@!!   @!!!:  @!!        @!!        @!@  !@! @!!!:!   @!@  !@!
#     !:!     !!: !!:        !!:        !!:  !!! !!:       !: .:! 
# ::.: :  ::: ::  : ::.: :    :         :: :  :  : :: :::    ::   
                                                                                                                              
# link  https://github.com/S3LTDev/Authentication
# author  max2tz https://github.com/S3LT
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

