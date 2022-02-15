import random
repeat = True

print("Welcome to R.P.S")
print("Do you wish to start the game? Y/N")

request = input()

if request in ["y","yes"]:
    print("okay, lets go")
else:
    exit()

while repeat:

    arrayStr = random.choice(["scissors", "paper", "rock"])  
    
    print("please enter (R)ock, (S)cissors or (P)aper")
    inn = input()



    if inn in ["rock","r"]:
        value = 1
        if arrayStr in ["rock"]:
            valueB = 1
        if arrayStr in ["paper"]:
            valueB = 2
        if arrayStr in ["scissors"]:
            valueB = 0

    if inn in ["scissors","s"]:
        value = 1
        if arrayStr in ["rock","r"]:
            valueB = 2
        if arrayStr in ["paper","p"]:
            valueB = 0
        if arrayStr in ["scissors","s"]:
            valueB = 1
        
    if inn in ["paper","p"]:
        value = 1
        if arrayStr in ["rock","r"]:
            valueB = 0
        if arrayStr in ["paper","p"]:
            valueB = 1
        if arrayStr in ["scissors","s"]:
            valueB = 2

    
    print(arrayStr)  

    if value == valueB:
        print("tie, ähnlich wie ne Krawatte")
    
    if value > valueB:
        print("you win! gz")
    
    if value < valueB:
        print("you lose!")

    print("btw, welcome to rps-hell! You will never escape lol")
    





    

    
    

