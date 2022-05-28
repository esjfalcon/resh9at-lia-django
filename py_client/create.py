import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'this is a title'
}

get_res = requests.post(endpoint, json=data)

print(get_res.json())