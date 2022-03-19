import requests
from datetime import datetime, timedelta
import time
from os import environ
from bet import info
#Define all the constants
time_interval = 60 # (in seconds) Specify the frequency of code execution
PINCODE = "801503"
tele_auth_token = "5220679875:AAHnEP49VI2oRJHFu_jy9yrj-eJQaKi7CUw" # Authentication token provided by Telegram bot
tel_group_id = "-641968281"     # Telegram group name
slot_found =  False                        # Intial slot found status
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
name="main" 
def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id={tel_group_id}&text={msg}"
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code == 200:
     print ("Notification has been sent on Telegram") 
    else:
     print ("Could not send Message")

if name == "main":    
     while True:
        data=info()
        print("INFO: %s" %data)
        if data!= "":
            send_msg_on_telegram(r"{}".format(data))
        
        
        time.sleep(time_interval)