import requests
import json

data = { 'text' : 'guinho guinho lucy bebe lucy thor thor pancho enter your text'}
headers = {'Accept': 'application/json',
            'Content-Type': 'application/json'}
url = 'http://localhost:8080/contagem'

# TODO: create exception classes for status codes. see other projects
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(response.text)
    elif response.status_code == 404:
        print("404 - Not Found")
    else:
        print(response.status_code + ": An error occurred.")
except:
    print("no go.")