import random

repeat = True


# define function
while repeat:
    diceRoll = random.randrange(1, 7)

    print("You just rolled a: ", diceRoll)
    if (diceRoll == 6):
        print("yeeeh")

    request = input("Roll again? Y/N ")

    if request in ["y","yes"]:
        repeat = True

    else:
        repeat = False 
        break

    

 