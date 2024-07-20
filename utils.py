import requests
import json
import re
import pandas as pd

def get_histories_1min():
    url = 'http://103.75.182.201:5000/get_data_ohlc_1min'    
    response = requests.get(url)
    data = response.json()
    data_df1 = []
    for i in data:
        time_ = i['time']
        time_ = pd.to_datetime(time_, format='%Y-%m-%d %H:%M:%S')
        time_ = time_ + pd.Timedelta(hours=7)
        # conver to format='%Y-%m-%dT%H:%M:%S.%fZ'
        time_ = time_.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        
        o = i['open']
        c = i['close']
        h = i['high']
        l = i['low']
        data_df1.append([time_, o, h, l, c])
        # đổi ngược đầu lên cuối
    data_df1 = data_df1[::-1]
    df1 = pd.DataFrame(data_df1, columns=['date', 'open', 'high', 'low', 'close'])
    # save to csv file ohlc.csv
    df1.to_csv('ohlc.csv', index=True)
    
    
def get_last_price():
    with open('ohlc.csv', 'r') as f:
        data = f.readlines()
        close_price = data[-1].split(',')[5]
        return float(close_price)

def get_data_new_round_1(input_string):
    input_string = input_string.replace('\\', '')
    input_string = input_string.replace('\"', '"')
    input_string = re.search(r"\[.*\]", input_string).group()
    input_string = input_string.replace('"{' , '{')
    input_string = input_string.replace('}"' , '}')
    # Chuyển đổi phần JSON từ chuỗi sang đối tượng Python
    json_part = json.loads(input_string)
    if json_part[0] == 'games/NEW_ROUND_1':
        json_part = json_part[1]
        return json_part
    
def get_start_live_round_1(input_string):
    input_string = input_string.replace('\\', '')
    input_string = input_string.replace('\"', '"')
    input_string = re.search(r"\[.*\]", input_string).group()
    input_string = input_string.replace('"{' , '{')
    input_string = input_string.replace('}"' , '}')
    # Chuyển đổi phần JSON từ chuỗi sang đối tượng Python
    json_part = json.loads(input_string)
    if json_part[0] == 'games/START_LIVE_ROUND_1':
        json_part = json_part[1]
        return json_part
    
def get_data_last_price(input_string):
    input_string = input_string.replace('\\', '')
    input_string = input_string.replace('\"', '"')
    input_string = re.search(r"\[.*\]", input_string).group()
    input_string = input_string.replace('"{' , '{')
    input_string = input_string.replace('}"' , '}')
    # Chuyển đổi phần JSON từ chuỗi sang đối tượng Python
    json_part = json.loads(input_string)
    if json_part[0] == 'users/UPDATE_LAST_PRICE':
        json_part = json_part[1]
        return json_part


def get_data_last_round(input_string):
    input_string = input_string.replace('\\', '')
    input_string = input_string.replace('\"', '"')
    input_string = re.search(r"\[.*\]", input_string).group()
    input_string = input_string.replace('"{' , '{')
    input_string = input_string.replace('}"' , '}')
    # Chuyển đổi phần JSON từ chuỗi sang đối tượng Python
    json_part = json.loads(input_string)
    if json_part[0] == 'games/LIVE_ROUND_COMPLETED_1':
        json_part = json_part[1]
        return json_part
    
    
def get_id_session():
    with open('data/id_session.txt', 'r') as f:
        id_session = f.read()
        return id_session.strip()
    
    
def call_check_key(key,log):
    url = f"http://103.75.182.201:5000/log_key?key={key}"
    payload = json.dumps(log)
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()