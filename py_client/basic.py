import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Anothe title", 'contnet':'another content', 'price': 3.29}) #API 
# print(get_response.text) # print the body response
# print(get_response.status_code)
print(get_response.json())
