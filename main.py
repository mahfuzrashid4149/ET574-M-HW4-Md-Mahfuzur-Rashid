# Name: Md Mahfuzur Rashid
# QCC ID: 24900040

import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)