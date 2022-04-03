from importlib.machinery import SourceFileLoader
import unittest

MODULE_PATH = "C:/Users/tolga/OneDrive/Masaüstü/python-topics/Testing/project/my_app/__init__.py"
MODULE_NAME = "my_app"

my_app = SourceFileLoader(MODULE_NAME, MODULE_PATH).load_module()

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.app = my_app.App(database='fixtures/test_basic.json')# Load test data but not defined 

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id = 10)
        self.assertEqual(customer['name'] , "org XYZ")
        self.assertEqual(customer['address'] , "10 Red Road, Reading")

class TestComplexData(unittest.TestCase):
    def setUp(self):
        self.app = my_app.App(database='fixtures/test_complex.json')# load test data but not defined

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer['name'], u"バナナ")
        self.assertEqual(customer['address'], "10 Red Road, Akihabara, Tokyo")


if __name__ == '__main__':
    unittest.main()