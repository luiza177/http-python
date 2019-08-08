import unittest
import bottle
from boddle import boddle
from word_counter_json_server import Word_Bottle

class TestServer(unittest.TestCase):
    
    def test_contagem_success(self):
        with boddle(json={'text':'shit'}):
            self.assertEqual(Word_Bottle.do_count_words(), { 'shit': 1 })
            
    def test_contagem_fail(self):
        with boddle(json={'t':'shit'}):
            self.assertRaises(bottle.HTTPError, Word_Bottle.do_count_words)
    
    def test_404(self):
        pass

if __name__ == '__main__':
    unittest.main()