import requests

endpoint = "http://localhost:8000/api/products/1/"

get_res = requests.get(endpoint)

print(get_res.json())