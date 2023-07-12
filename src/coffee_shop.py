class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

	def change_till_by_amount(self, amount):
		self.till += amount



	def age_check(self, customer):
		result = customer.get_age()
		if result < 16:
			return False #under 16
		if result >= 16:
			return True #16 or over
		
	def sell_drink(self, customer, drink):
		check_age_result = self.age_check(customer)
		if check_age_result == False:
			return "Customer is underage"
		check_energy_result = self.energy_check(customer)
		if check_energy_result == False:
			return "You have had too much coffee"
		else:
			drink_price = customer.buy_drink(drink)
			self.change_till_by_amount(drink_price)
			return "Enjoy your coffee"

	
	def energy_check(self, customer):
		result = customer.get_energy_level()
		if result > 150:
			return False
		