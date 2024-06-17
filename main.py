import DND1


def main():

    dnd_player_1 = DND1.DNDice()
    diceSelected = dnd_player_1.userInputDiceSelection()
    numberOfRolls = dnd_player_1.userInputRolls()
    total = dnd_player_1.roll(numberOfRolls, diceSelected)
    print(f"The total of the dice is: {total}")


if __name__ == "__main__":
    main()
