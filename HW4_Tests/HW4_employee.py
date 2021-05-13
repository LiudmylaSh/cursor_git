import requests
import unittest
from unittest.mock import patch

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'



class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee1 = Employee("Jane", "Brown", 9999)
        self.employee2 = Employee("Santa", "Ling", 0)
        self.employee3 = Employee("Mary", "Bing", 200)
        self.employee4 = Employee("John", "Willing", None)

    def test_email(self):
        self.assertEqual(self.employee1.email, "Jane.Brown@email.com")
        self.assertEqual(self.employee2.email, "Santa.Ling@email.com")
        self.assertEqual(self.employee3.email, "Mary.Bing@email.com")
        self.assertEqual(self.employee4.email, "John.Willing@email.com")

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname, "Jane Brown")
        self.assertEqual(self.employee2.fullname, "Santa Ling")
        self.assertEqual(self.employee3.fullname, "Mary Bing")
        self.assertEqual(self.employee4.fullname, "John Willing")

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 10498)
        self.employee2.apply_raise()
        self.assertEqual(self.employee2.pay, 0)
        self.employee3.apply_raise()
        self.assertEqual(self.employee3.pay, 210)
        with self.assertRaises(TypeError):
            self.employee4.apply_raise()
        self.assertEqual(self.employee4.pay, None)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get_response):
        mock_get_response.return_value.ok = True
        self.assertEqual(self.employee1.monthly_schedule("January"), mock_get_response().text)
        self.assertEqual(self.employee2.monthly_schedule("April"), mock_get_response().text)
        mock_get_response.return_value.ok = False
        self.assertEqual(self.employee3.monthly_schedule("May"), "Bad Response!")
        self.assertEqual(self.employee4.monthly_schedule("May"), "Bad Response!")
