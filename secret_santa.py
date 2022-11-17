from random import shuffle

players = ["Tracy", "Hannah", "Braxton", "Adri"]

givers = players.copy()
shuffle(givers)

receivers = players.copy()
shuffle(receivers)



results = {}

all_gifted = len(givers)
while all_gifted > len(results):
    for giver, receiver in zip(givers, receivers):
        if giver != receiver:
            print("gift!")
            results[giver] = receiver
        else:
            print("no gift, try again!")
            shuffle(givers)
            shuffle(receivers)

for santa, receiver in results.items():
    print(f"{santa} gives a gift to {receiver}!")
