import unittest
from unittest.mock import patch
from word_counter_client import Word_Counter_Client

class TestWordCounterClient(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_post_word_counter_api(self):
        with patch('word_counter_client.requests.post') as mock_post:
            mock_post.return_value.ok = True
            mock_post.return_value.text = "Bebebol"

            client = Word_Counter_Client({ 'text' : 'bebezinho bol' })
            response = client.post_request()
            self.assertEqual(response, 'Bebebol')

            mock_post.return_value.ok = False
            response = client.post_request()
            self.assertEqual(response, 'POST Request failed!')
            






if __name__ == '__main__':
    unittest.main()