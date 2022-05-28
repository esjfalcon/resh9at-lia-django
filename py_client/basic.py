
import requests

endpoint = "http://localhost:8000/api/"

get_res = requests.post(endpoint, json={'title':'title 1','content':'hello again'})

print(get_res.json())