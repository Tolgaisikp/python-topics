import unittest
from fractions import Fraction
from importlib.machinery import SourceFileLoader

MODULE_PATH = "C:/Users/tolga/OneDrive/Masaüstü/python-topics/Testing/project/my_sum/__init__.py"
MODULE_NAME = "my_sum"

my_sum = SourceFileLoader(MODULE_NAME, MODULE_PATH).load_module()


class TestSum(unittest.TestCase):
    def test_list_sum(self): #Can it sum a list of whole numbers (integers)?
        data = [1,2,3]
        result = my_sum.sum(data)
        self.assertEqual(result, 6)

    def test_fraction_sum(self): #Can it sum a list of floats?
        data  = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = my_sum.sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self): #What happens when you provide it with a bad value, such as a single integer or a string?
        data = 'banana'
        with self.assertRaises(TypeError):# This test case will now only pass if sum(data) raises a TypeError
            result = my_sum.sum(data)

if __name__ == '__main__':
    unittest.main()


