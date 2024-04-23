from datetime import datetime
import requests
import json
import pandas as pd

def is_holiday(user_date):
    key='보안키'
    RestDay='getRestDeInfo'
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/'+RestDay
    params ={'serviceKey' : key, 'numOfRows' : '100', '_type':'json', 'solYear' : str(datetime.today().year)}

    response = requests.get(url, params=params)

    result=json.loads(response.text)
    json.dumps(result,indent=4,ensure_ascii=False)
    The_holiday=[]
    for i in range(len(result ['response']['body']['items']['item'])):
        The_holiday.append(result['response']['body']['items']['item'][i]['locdate'])
    if user_date in The_holiday:
        return False
    else:
        return True
