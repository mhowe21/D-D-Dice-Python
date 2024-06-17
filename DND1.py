import random

# class for imput for dice type


class DNDice:
    def __init__(self):
        self.timesRolled = 0

    def roll(self, num_rolls, dicetype):
        """
        Rolls a dice multiple times and prints the result of each roll.

        Args:
            num_rolls (int): The number of times to roll the dice.

        Returns:
            sum of dice rolls (int): The sum of the dice rolls.
        """
        self.dicetype = dicetype
        self.num_rolls = int(num_rolls)
        self.sumOfRolls = 0
        self.diceResult = 0
        for i in range(self.num_rolls):
            self.timesRolled += 1
            self.diceResult = random.randint(1, int(self.dicetype))
            print(f"Roll {i+1}: {self.diceResult}")
            self.sumOfRolls += self.diceResult
        return self.sumOfRolls

    def userInputDiceSelection(self):
        """
        Prompts the user to enter the number of sides for a dice and validates the input.

        This function repeatedly prompts the user to enter the number of sides for a dice until a valid integer is entered. It uses a while loop to continue prompting the user until a valid input is provided. The input is converted to an integer using the `int()` function and stored in the `dicetype` attribute of the instance.

        Parameters:
            self (object): The instance of the class.

        Returns:
            int: The number of sides entered by the user.

        Raises:
            ValueError: If the user enters an invalid input (not an integer).
        """

        self.dicetype = 0
        self.validInput = False
        while self.validInput == False:
            try:
                self.dicetype = int(input("Enter the number of sides: "))
                self.validInput = True
            except ValueError:
                print("Invalid input. Please enter a number.")

        return self.dicetype

    def userInputRolls(self):
        """
        Prompts the user to enter the number of rolls and validates the input.

        This function repeatedly prompts the user to enter the number of rolls until a valid integer is entered. It uses a while loop to continue prompting the user until a valid input is provided. The input is converted to an integer using the `int()` function and stored in the `rolls` attribute of the instance.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None

        Raises:
            ValueError: If the user enters an invalid input (not an integer).
        """
        self.rolls = 0
        self.validInput = False
        while self.validInput == False:
            try:
                self.rolls = int(input("Enter the number of rolls: "))
                self.validInput = True
            except ValueError:
                print("Invalid input. Please enter a number.")
        return self.rolls
