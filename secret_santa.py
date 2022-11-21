## Simon Uribe - 2022-11-21

## Input a list of names below with the people who will be playing Secret Santa
## You can include each person's address after their name, separated by a space, `@`, and a space.
## for example ["Batman @ The Batcave", "The Penguin @ The Iceberg Lounge", "Robin @ The Circus", "Mr. Freeze @ Gotham Mercy Hospital"]
## the addresses are handy to have in case you are copy/pasting the output to emails or Slack messages
## It prints out a table at the end in case that's useful!

# Enjoy!


from __future__ import annotations
from random import shuffle
import pandas as pd

## without addresses
## players = ["Batman", "The Penguin", "Robin", "Mr. Freeze"]

# with addresses
players = ["Batman @ The Batcave", "The Penguin @ The Iceberg Lounge", "Robin @ The Circus", "Mr. Freeze @ Gotham Mercy Hospital"]


def play_secret_santa(players: list[str], address: bool=False) -> dict:
    """Randomizes a list of names to play Secret Santa

    :param list[str] players: List of names of people who are playing
    :param bool address: Set to True if the list of names includes each participant's address.
    The address must be after their name, separated by a space, `@`, and a space. This parameter defaults to False.
    :return dict: Dictionary with secret Santa as key and receiver as value
    """    
    
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

    if address:
        for santa, receiver in results.items():
            print(f"\n\nDear {santa.split(' @ ')[0]}, you are giving a gift to {receiver.split(' @ ')[0]}!\n\n Their address is:\n {receiver.split(' @ ')[1]}\n\n Cheers!\n 🧝")
            print("\n\n\n---------\n")
    else:
        for santa, receiver in results.items():
            print(f"\n\nDear {santa}, you are giving a gift to {receiver}!\n\n Cheers!\n 🧝")
            print("\n\n\n---------\n")
    
    return results


# Run it
results = play_secret_santa(players, address=True)


# Print a table in case that's useful 
santas_df = pd.DataFrame.from_dict(results, orient="index", columns=["Gift receiver"])
santas_df.index.name = "Secret Santa"
santas_df
