import random
coin = random.choice(["head", "tail"])
count = random.randint(1, 10)
print(coin)
print(count)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

