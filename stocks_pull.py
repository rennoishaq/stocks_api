import requests
import json
from psycopg2 import pool

url = 'https://api.worldtradingdata.com/api/v1/history'
params = {
    'symbol': 'PINS',
    'api_token': 'ARb17i5xIu5Q40bESJM0b1BCNgpBVtRgwxppgTmnI0LHwFEepE02AC85HIYF',
    'date_from': '2018-01-01',
    'sort': 'asc'
}
s = requests.request('GET', url, params=params)
s_json = s.json()

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user='postgres',
                                            password='rendino12',
                                            database='learning',
                                            host='localhost')

with connection_pool.getconn() as connection:
    with connection.cursor() as cursor:
        cursor.executemany('INSERT INTO stock_price (history,open,close,high,low,volume) VALUES (%(history)s,'
                           '%(open)s, %(close)s, %(high)s, %(low)s, %(volume)s)', s_json)

