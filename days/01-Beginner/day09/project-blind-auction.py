import os

bids = {}
next_bid = "yes"

while next_bid == "yes":
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    next_bid = input("\nAre there any other bidders? Type 'yes or 'no'.\n").lower()
    os.system('clear')

winner = max(bids.items(), key = lambda x: x[1])

print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
