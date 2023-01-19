import requests

endpoint ='http://localhost:8000/products/new/'

data={
    "title": "from py_client create",
    "content": "This is from hte endpoint",
    "price": 5.79
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())

#get_response = requests.post(endpoint, json=data)

#print(get_response.json())