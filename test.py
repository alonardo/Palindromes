from unittest import TestCase, main

from palindrome import palindrome1, palindrome2, palindrome3

class MatchTestCase(TestCase):
    def test_1_basic_palindrome(self):
        self.assertEqual(palindrome1('racecar'), True)
    def test_2_palindrome_with_spaces_nonalpha(self):
        self.assertEqual(palindrome1('A man, a plan, a canal: Panama'), True )
    def test_3_not_palindrome(self):
        self.assertEqual(palindrome1("race a car"), False )
    def test_4_uppercase_nonalpha(self):
        self.assertEqual(palindrome1("$%RACECAR"), True)

    def test_5_basic_palindrome(self):
        self.assertEqual(palindrome2('racecar'), True)
    def test_6_palindrome_with_spaces_nonalpha(self):
        self.assertEqual(palindrome2('A man, a plan, a canal: Panama'), True )
    def test_7_not_palindrome(self):
        self.assertEqual(palindrome2("race a car"), False )
    def test_8_uppercase_nonalpha(self):
        self.assertEqual(palindrome2("$%RACECAR"), True)

    def test_9_basic_palindrome(self):
        self.assertEqual(palindrome3('racecar'), True)
    def test_10_palindrome_with_spaces_nonalpha(self):
        self.assertEqual(palindrome3('A man, a plan, a canal: Panama'), True )
    def test_11_not_palindrome(self):
        self.assertEqual(palindrome3("race a car"), False )
    def test_12_uppercase_nonalpha(self):
        self.assertEqual(palindrome3("$%RACECAR"), True)

if __name__ == '__main__':
    main()