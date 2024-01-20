import requests
import threading
import time
import os
from dotenv import load_dotenv

def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def detect(token, period_minute):
   counter = 0
   while True:
        counter = counter + 1
        message = f"\n基本功能測試\n 訊息{counter}"
        lineNotifyMessage(token, message)
        time.sleep(period_minute * 60)
      
if __name__ == "__main__":
  load_dotenv()
  token = os.getenv("NOTIFY_TOKEN")
  period_minute = os.getenv("DETECT_PERIOD_MINUTE")
  thread = threading.Thread(target=detect, args=(token, period_minute))
  thread.start()