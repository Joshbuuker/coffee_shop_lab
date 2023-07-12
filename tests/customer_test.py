import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Paul", 25, 18, 50)
        self.drink = Drink("Mocha", 10, 25)

    def test_customer_has_name(self):
        self.assertEqual("Paul", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(25, self.customer.wallet)
    
    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(15, self.customer.wallet)

    def test_customer_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(15, self.customer.wallet)
    
    def test_customer_get_age(self):
        return_age = self.customer.get_age()
        self.assertEqual(self.customer.age, return_age)
    
    def test_customer_energy_level(self):
        return_energy = self.customer.increase_energy_level(self.drink)
        self.assertEqual(75, return_energy)