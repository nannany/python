import requests

url = 'https://bitflyer.jp/api/echo/price'

r = requests.get(url)

print(r)
print(r.text)
