import random  

type = ["a", "b", "c", "d"]
nums = list(range(1, 11))

typeNums = []
shuffledDeck = []

# x = element in array
for x in type:
    # y = element in nums
    for y in nums:
        z = x, str(y)
        # z = teil von deck
        typeNums.append(z)

# shuffle
for i in range(0, len(typeNums)):

    index = random.randint(0, len(typeNums) - 1)
    # random element(index) aus typeNums
    shuffle = typeNums[index]
    # move
    shuffledDeck.append(shuffle)

    typeNums.remove(shuffle)

print("shuffled: ", shuffledDeck)
print(typeNums)

players = []

# 4 Player x 4 iterations
for i in range(0, 4):
    player = []
    # 5 cards each x 5 iterations
    for j in range(0, 5):
        # first card from sD in player array
        player.append(shuffledDeck[0])
        # remove first card
        shuffledDeck.remove(shuffledDeck[0])
    # move player array to playerGroup array [[],[],[],[]]      
    players.append(player)

print(players)


    




    