import json
import requests

endpoint = "http://localhost:8000/api/"

get_res = requests.get(endpoint, params={'abc':123}, json={'query':'helloworld'})

print(get_res.json())