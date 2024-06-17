import random

# class for imput and rolls for DnD dice


class DNDice:
    def __init__(self):
        # initializes an instance of the DNDice class
        """
        Initializes an instance of the DNDice class.

        This constructor sets the initial value of the `timesRolled` attribute to 0.
        The `timesRolled` attribute keeps track of the number of times the dice has been rolled.

        Parameters:
            self (DNDice): The instance of the DNDice class.

        Returns:
            None
        """
        self.timesRolled = 0

    def roll(self, numRolls, dicetype):
        # this method rolls a dice a set multiple of times based on the numb_rolls input and prints the result of each roll
        """
        Rolls a dice a set multiple of times based on the numb_rolls input and prints the result of each roll.

        Args:
            numRolls (int): The number of times to roll the dice.

        Returns:
            sum of dice rolls (int): The sum of the dice rolls.
        """
        self.dicetype = dicetype
        self.numRolls = int(numRolls)
        self.sumOfRolls = 0
        self.diceResult = 0
        for i in range(self.numRolls):
            self.timesRolled += 1
            self.diceResult = random.randint(1, int(self.dicetype))
            if self.diceResult == 20 and self.dicetype == 20:
                print(f"Roll {i+1}: {self.diceResult}! Critical Success!!")
            elif self.diceResult == 1 and self.dicetype == 20:
                print(f"Roll {i+1}: {self.diceResult}! Critical failure...")
            else:
                print(f"Roll {i+1}: {self.diceResult}")
            self.sumOfRolls += self.diceResult
        return self.sumOfRolls

    def userInputDiceSelection(self):
        # this method prompts the user to enter the number of sides for a dice and validates the input
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
        # this loop runs until the user enters a valid input
        while self.validInput == False:
            try:
                self.dicetype = abs(
                    int(input("Enter the number of sides on the dice: ")))
                if self.dicetype > 0:
                    self.validInput = True
                else:
                    self.validInput = False
            except ValueError:
                print("Invalid input. Please enter a number.")

        return self.dicetype

    def userInputRollSelection(self):
        # this method prompts the user to enter the number of rolls and validates the input
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
                self.rolls = abs(int(input("Enter the number of rolls: ")))
                if self.rolls > 0:
                    self.validInput = True
                else:
                    self.validInput = False
            except ValueError:
                print("Invalid input. Please enter a number.")
        return self.rolls

    def getNumberOfTimesRolled(self):
        # this method returns the number of times the dice has been rolled
        """function that returns the number of times the dice has been rolled

        Returns:
            int: total number of times the dice has been rolled
        """
        return self.timesRolled
