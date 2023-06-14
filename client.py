import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/safety/8"


endpoint2 = "http://127.0.0.1:8000/api/create"

endpoint3 = "http://127.0.0.1:8000/api/auth/"
endpoint4 = "http://127.0.0.1:8000/api/all"

password = getpass()

data = requests.post(endpoint3 ,json={"username":"pmk","password":password})

if data.status_code == 200:
    token = data.json()["token"]
    headers = {
        "Authorization":f"Token {token}"
    }
    req = requests.get(endpoint4,headers=headers)

    print(req.json()["count"]) 