import requests

api = '1y6DX14caIg7mBLjNcdLQQMtCt5TvykgdKhuUpMfr4q9CaDfRP9yd967l66Dg7uh'
key = '1f3VAyMMC5arWRJxNrOw5frXkZAVYMUuHaHH3nysoGkLkntHsr8ihHUEx6zn1EVq'
base_url = 'https://fapi.binance.com'
endpoint = '/fapi/v1/ticker/24hr'
symbol = 'REZUSDT'
url = f"{base_url}{endpoint}?symbol={symbol}"
headers ={
    'X-MBX-APIKEY': api
}
response = requests.get(url, headers=headers)
data = response.json()

# Print the data
print(data)




















