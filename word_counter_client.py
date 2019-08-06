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
        result_dict = {}
        try:
            response = requests.post(self._url, headers=self._headers, data=json.dumps(self.data))
            if response.ok:
                result_dict = response.json()
        except requests.HTTPError as e:
            result_dict["ERROR"] = e
        except requests.ConnectTimeout as e:
            result_dict["ERROR"] = "Your connection was timed out."
        except requests.ConnectionError as e:
            result_dict["ERROR"] = "Make sure you are connected to the internet."

        return result_dict


if __name__ == '__main__':
    client = Word_Counter_Client.test_data()
    print(client.post_request())