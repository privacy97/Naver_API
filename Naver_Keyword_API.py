import time
import random
import requests
import pandas as pd

import signaturehelper


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
r = requests.get(BASE_URL + uri+'?hintKeywords={}&showDetail=1'.format('파이썬'),
                 headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

df = pd.DataFrame(r.json()['keywordList'])
print(df.head())


# DevTools failed to load SourceMap

# uncaught typeerror cannot read
