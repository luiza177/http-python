import requests
import json

class NotFound(Exception):
	pass

class BadRequest(Exception):
	pass

class UnexpectedError(Exception):
	pass

data = { 'text' : 'guinho guinho lucy bebe lucy thor thor pancho enter your text'}
headers = {'Accept': 'application/json',
            'Content-Type': 'application/json'}
url = 'http://localhost:8080/contagem'

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(response.text)
    response.raise_for_status()
except requests.HTTPError as e:
    print(e)
except requests.ConnectTimeout as e:
    # print(e)
    print("Your connection was timed out.")
except requests.ConnectionError as e:
    # print(e)
    print("Make sure you are connected to the internet.")