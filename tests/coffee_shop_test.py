import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.customer = Customer("Paul", 25, 18, 120)
        self.customer2 = Customer("Mike", 10, 8, 150)
        self.drink = Drink("Mocha", 10, 25)


    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)
    
    def test_coffee_shop_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)
    
    def test_coffee_shop_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)
    
    def test_coffee_shop_sell_drink(self):
        self.coffee_shop.sell_drink(self.customer, self.drink)
        result = self.coffee_shop.sell_drink(self.customer2, self.drink)
        self.assertEqual(110, self.coffee_shop.till)
        self.assertEqual(15, self.customer.wallet)
        self.assertEqual("Customer is underage", result)
    
    def test_age_check(self):
        result1 = self.coffee_shop.age_check(self.customer)
        result2 = self.coffee_shop.age_check(self.customer2)
        self.assertEqual(True, result1)
        self.assertEqual(False, result2)
    
    def test_energy_check(self):
        result1 = self.coffee_shop.energy_check(self.customer)
        result2 = self.coffee_shop.energy_check(self.customer2)
        self.assertEqual(True, result1)
        self.assertEqual(False, result2)