import requests

url = "https://api.coinlore.net/api/tickers/"
response = requests.get(url)

print(response.json())