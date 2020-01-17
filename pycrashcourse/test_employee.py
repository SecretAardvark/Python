import unittest
from employee import Employee

class testEmployee(unittest.TestCase):
    def setUp(self):
        self.chad = Employee('Chad', 'Tennent', 20000)

    def test_give_default_raise(self):
        self.chad.give_raise()
        self.assertEqual(self.chad.salary, 25000)

    def test_give_custom_raise(self):
        self.chad.give_raise(10000)
        self.assertEqual(self.chad.salary, (30000))


unittest.main()