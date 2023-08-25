import requests


url = 'http://localhost:8000/one-string/'
# response = requests.get(url=url)
# data = response.json()
# print("Type of request: ", type(data), "Data: ", data)

text = {'textinput': 'test_text'}
response = requests.post(url, data=text)
print(response.content)

