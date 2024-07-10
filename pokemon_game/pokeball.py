from random import random
from item import Item

class Pokeball(Item):
    def __init__(self, name, catch_rate):
        super().__init__(name, 'Pokeball', self.catch)
        self.catch_rate = catch_rate

    def attempt_catch(self, wild_pokemon):
        return random() < self.catch_rate
