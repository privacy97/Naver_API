import time
import random
import requests
import pandas as pd

import signaturehelper

Keyword_list = [
    '빵',
    '식빵',
    '단팥빵',
    '호밀빵'
]

DataFrame_list = []


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(
        timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp, 'X-API-KEY': API_KEY,
            'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


BASE_URL = 'https://api.naver.com'
API_KEY = ''
SECRET_KEY = ''
CUSTOMER_ID = ''

uri = '/keywordstool'
method = 'GET'

for Keyword in Keyword_list:
    query = {
        'siteId': '',
        'biztpId': '',
        'hintKeywords': Keyword,
        'event': '',
        'month': 12,
        'showDetail': 0,
    }

    r = requests.get(BASE_URL + uri,
                     params=query,
                     headers=get_header(
                         method=method,
                         uri=uri,
                         api_key=API_KEY,
                         secret_key=SECRET_KEY,
                         customer_id=CUSTOMER_ID
                     ))

    r_data = r.json()
    temp = r_data['keywordList'][0]

    temp['키워드'] = temp.pop('relKeyword')
    temp['월평균_PC'] = temp.pop('monthlyPcQcCnt')
    temp['월평균_Moblie'] = temp.pop('monthlyMobileQcCnt')

    DataFrame_list.append(r_data['keywordList'][0])


df = pd.DataFrame(DataFrame_list)
print(df)

file_name = 'Keyword_Query_List.xlsx'
df.to_excel(file_name, index=False)
