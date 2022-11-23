import unittest

from codeChallenges.pythonchallenge import challenge5


class Test_Palindrome_Check(unittest.TestCase):

    def test_palindrome_check(self):
        self.assertEqual(challenge5.palindrome_check("madam"), 'madam: This is a Palindrome')
        self.assertEqual(challenge5.palindrome_check("boss"), 'boss: This is not a Palindrome')