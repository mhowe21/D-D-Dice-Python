import DND1


def main():
    # setting the play game to ture to start the game
    continueRolling = True
    # check to make sure the input that a user provides if they would like to play again is valid
    inputValidation = True
    # create an object of the DND1 class to use its functions
    dnd_player_1 = DND1.DNDice()

    # this starts the rolling process and exits when the user selects no or n
    while inputValidation == True and continueRolling == True:
        # this uses the userInputDiceSelection and userInputRollSelection functions to get the user's input
        diceSelected = dnd_player_1.userInputDiceSelection()
        numberOfRolls = dnd_player_1.userInputRollSelection()
        # this total is caculation that pulls the given value from the roll function
        total = dnd_player_1.roll(numberOfRolls, diceSelected)
        print(f"The total of the dice is: {total}")

        # this asks the user if they would like to roll again if they select n or no it exits the program or if they select y or yes it starts the rolling process again
        playAgain = input("Do you want to roll again? (y/n): ")
        if playAgain.lower() == "y" or playAgain.lower() == "yes":
            continueRolling = True
        elif playAgain.lower() == "n" or playAgain.lower() == "no":
            print("Thanks for rolling with us!")
            continueRolling = False
        else:
            inputValidation = False
            while inputValidation == False:
                playAgain = input(
                    "Invalid input. Do you want to roll again? (y/n): ")
                if playAgain.lower() == "y" or playAgain.lower() == "yes":
                    continueRolling = True
                    inputValidation = True
                elif playAgain.lower() == "n":
                    print("Thanks for rolling with us!")
                    continueRolling = False
                    inputValidation = True
                else:
                    inputValidation = False


if __name__ == "__main__":
    main()
