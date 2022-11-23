import unittest

from codeChallenges.pythonchallenge import challenge2


class Testpowerofnumber(unittest.TestCase):

    def test_powerofnumber(self):
        self.assertEqual(challenge2.powerofnumber(4, 2), 16)

