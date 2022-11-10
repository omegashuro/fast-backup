import unittest
import mastermind
from io import StringIO
from unittest.mock import patch
import sys

class myTest(unittest.TestCase):

    def test_my_test(self):
        i = 0
        while i< 100:
            actual = len(mastermind.create_code())
            expected = 4
            self.assertEqual(actual, expected)
            i+=1


    
    def test_check_correctness(self):
        self.assertTrue(mastermind.check_correctness(12,4))
        self.assertFalse(mastermind.check_correctness(11,3))
        self.assertFalse(mastermind.check_correctness(1,2))
        self.assertFalse(mastermind.check_correctness(5,1))


    @patch("sys.stdin", StringIO("123\n1234\n"))
    def test_get_answer_input(self):
        output = StringIO()
        sys.stdout = output

        ans = mastermind.get_answer_input()

        # self.assertEqual(, "Please enter exactly 4 digits.")
        self.assertEqual(ans, "1234")
        self.assertEqual("Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ", output.getvalue())

        

      