class Customer:
    def __init__(self, name, wallet, age, energy):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = energy

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        drink_price = drink.price
        self.reduce_wallet(drink_price)
        return drink_price
    
    def get_age(self):
        return self.age

    def get_energy_level(self):
        return self.energy
    
    def increase_energy_level(self, drink):
        caffeine_level = drink.caffeine_level
        self.energy += caffeine_level
        return self.energy