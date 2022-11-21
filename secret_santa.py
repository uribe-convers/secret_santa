from random import shuffle
import pandas as pd


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
            results[giver] = receiver
        else:
            shuffle(givers)
            shuffle(receivers)

for santa, receiver in results.items():
    print(f"Dear {santa}, you are giving a gift to {receiver}!")

 
santas_df = pd.DataFrame.from_dict(results, orient="index", columns=["Gift receiver"])
santas_df.index.name = "Secret Santa"
santas_df
