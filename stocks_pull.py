import requests
from psycopg2 import pool

url = 'https://api.worldtradingdata.com/api/v1/history'
params = {
    'symbol': 'PINS',
    'api_token': 'ARb17i5xIu5Q40bESJM0b1BCNgpBVtRgwxppgTmnI0LHwFEepE02AC85HIYF',
    'date_from': '2018-01-01',
    'sort': 'asc'
}
s = requests.request('GET', url, params=params)
print(s.json())

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user='postgres',
                                            password='rendino12',
                                            database='learning',
                                            host='localhost')

with connection_pool.getconn() as connection:
    with connection.cursor() as cursor:
        i = "INSERT INTO stock_price VALUES (%(name)s, %(history)s, %(open)s, %(close)s, %(high)s, %(low)s, %(volume)s)"
        cursor.execute(i, s)
