import requests

endpoint ='http://localhost:8000/products/list/'

get_response = requests.get(endpoint)

print(get_response.json())

#get_response = requests.post(endpoint, json=data)

#print(get_response.json())