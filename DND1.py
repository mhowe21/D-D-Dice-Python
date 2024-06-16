import random

# class for imput for dice type
class DNDice:
    def __init__(self, sides):
        self.sides = int(sides) # number of sides

    def setSides(self, sides):
        self.sides = int(sides)
        

    def roll(self, num_rolls):
        self.num_rolls = int(num_rolls)
        for i in range(self.num_rolls):
            print(f"Roll {i+1}: {random.randint(1, self.sides)}")
       
        