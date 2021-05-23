#from django.test import TestCase
import pytest
import unittest



#class InicialTestCase(TestCase):
class InicialTestCase(unittest.TestCase):

    def setUp(self):
      self.number = 1
      self.number_two = 2

    def test_one_plus_one_equals_two(self):
        """ Method: test_one_plus_one_equals_two. """  
        #assert (1 + 1, 2)
        assert True

    def test_sum(self):
        assert (2 + 2) == 4

    def test_sum_output_type(self):
        res = self.number + self.number_two
        self.assertIs(type(res), int)


if __name__ == '__main__':
    unittest.main()        