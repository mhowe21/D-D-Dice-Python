import DND1

def main():
    type = diceType()
    rolls = numberOfRolls()
    dnd_player_1 = DND1.DNDice(type)
    dnd_player_1.roll(rolls)

def diceType():
    sides = input("Enter the number of sides: ")
    return sides
def numberOfRolls():
    rolls = input("Enter the number of rolls: ")
    return rolls


    

if __name__ == "__main__":
    main()