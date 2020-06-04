
# write some code using unittest to test our enlarge() function works as desired

import unittest

from my_lambdata.my_mod import enlarge

class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(enlarge(9), 900)


if __name__ == '__main__':
    unittest.main() # invoking all of our test class's methods
