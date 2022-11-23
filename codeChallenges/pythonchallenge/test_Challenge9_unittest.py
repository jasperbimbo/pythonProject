import unittest

from codeChallenges.pythonchallenge import challenge9


class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_uppercase(self):
        self.assertEqual(challenge9.convert_string_uppercase("madam"), 'MADAM')
        self.assertEqual(challenge9.convert_string_uppercase("boss"), 'BOSS')
