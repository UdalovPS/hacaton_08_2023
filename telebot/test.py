import requests


url = 'http://localhost:8000/hac_app/about/?format=json'
response = requests.get(url=url)
data = response.json()
print("Type of request: ", type(data), "Data: ", data)
