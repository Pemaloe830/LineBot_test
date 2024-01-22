import requests
import threading
import time
import os
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from crawler import *

followSettingFileName = "followSetting.json"

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def detect(token, period_minute, json_data):
    #print(json_data)
    if ("boards" not in json_data or json_data["boards"] is None):
        raise Exception("尚未設定欲追蹤的看板資訊")
    crawler = Crawler(json_data["boards"])
    result = crawler.Start()
    #print(crawler.Start())

    while True:
        message = f"\n基本功能測試 - {', '.join(result)}"
        lineNotifyMessage(token, message)
        time.sleep(period_minute * 60)
      
if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("NOTIFY_TOKEN")
    period_minute = os.getenv("DETECT_PERIOD_MINUTE")
    current_project_path = os.getcwd() # 獲取當前專案的路徑（即應用程序運行的目錄）
    json_file_path = os.path.join(current_project_path, followSettingFileName)
    
    if os.path.getsize(json_file_path) > 0:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    else:
        raise Exception("json設定檔不可為空白")

    thread = threading.Thread(target=detect, args=(token, int(period_minute), json_data))
    thread.start()