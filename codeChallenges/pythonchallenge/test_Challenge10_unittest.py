import unittest

from codeChallenges.pythonchallenge import challenge10



class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_sentencecase(self):
        self.assertEqual(challenge10.convert_string_sentencecase("madam"), 'Madam')
        self.assertEqual(challenge10.convert_string_sentencecase("boss"), 'Boss')