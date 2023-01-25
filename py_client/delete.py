import requests

product_id = input("What is the product id you want:  ")
try:
    product_id = int(product_id)
except:
    product_id=None
    print(f'{product_id} not valid')

endpoint ='http://localhost:8000/products/{product_id}/delete'

get_response = requests.delete(endpoint)

print(get_response.status_code, get_response. status_code==204) 