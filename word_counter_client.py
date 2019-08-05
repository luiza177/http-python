import requests
import json

class Word_Counter_Client():

    _headers = {'Accept': 'application/json',
                'Content-Type': 'application/json'}
    _url = 'http://localhost:8080/contagem'
    
    def __init__(self, data):
        self.data = data
    
    @classmethod
    def test_data(cls):
        return cls(data = { 'text' : 'guinho guinho lucy bebe lucy thor thor pancho enter your text'})

    def post_request(self):
        try:
            response = requests.post(self._url, headers=self._headers, data=json.dumps(self.data))
            if response.ok:
                return response.text
        except requests.HTTPError as e:
            print(e)
        except requests.ConnectTimeout as e:
            print("Your connection was timed out.")
        except requests.ConnectionError as e:
            print("Make sure you are connected to the internet.")

        return 'POST Request failed!'


if __name__ == '__main__':
    client = Word_Counter_Client.test_data()
    print(client.post_request())