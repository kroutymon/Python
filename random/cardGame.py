import random

deckColour = ["a", "b", "c", "d"]
nums = list(range(1, 11))

deck = []
shuffledDeck = []

for x in deckColour:
    for y in nums:
        z = x, y
        deck.append(z)

while len(deck) > 0:
    index = random.randint(0,len(deck) - 1)
    card = deck[index]
    shuffledDeck.append(card)

    deck.remove(card)
    
print(deck)
print(shuffledDeck)



    





