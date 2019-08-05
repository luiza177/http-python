import unittest
import word_counter

class TestWordCounter(unittest.TestCase):

    def test_prep_for_analysis(self):
        text = "Bebezinho vai ser sempre meu Bebebol. Te amo, pequeno. 24/12/2008-1/8/2019 @"
        result = ['24122008182019', 'amo', 'bebebol', 'bebezinho', 'meu', 'pequeno', 'sempre', 'ser', 'te', 'vai']
        self.assertEqual(word_counter.prepare_for_analysis(text), result)

    def test_word_analysis(self):
        text = "Bebezinho, Bebebol. Te amo sempre, bebezinho. 24/12/2008-1/8/2019"
        result = { '24122008182019': 1, 'amo': 1, 'bebebol': 1, 'bebezinho': 2, 'sempre': 1, 'te': 1 }
        self.assertEqual(word_counter.word_analysis(text), result)

    def test_display_word_analysis(self):
        word_dict = {'bebezinho': 1, 'bebe': 2 }
        times_1 = round(1/3*100, 2)
        times_2 = round(2/3*100, 2)
        display = "<p>Word count: 3</p>"
        display += "<p><small><i>'bebezinho'</i> appears 1 times and consists of {0} percent of text.</small></p>".format(times_1)
        display += "<p><small><i>'bebe'</i> appears 2 times and consists of {0} percent of text.</small></p>".format(times_2)
        self.assertEqual(word_counter.display_word_analysis(word_dict), display)


if __name__ == '__main__':
    unittest.main()