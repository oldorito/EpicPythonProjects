import os

from silent_auction_art import logo
print(logo)

bids = {}
other_bidders = True

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while other_bidders:
    bidder_name = input("What is your name?\n")
    bid_price = input("What is your bid?\n$")
    
    bids["name"] = bidder_name
    bids["price"] = bid_price
    
    are_there_other_bidders = (input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if are_there_other_bidders == "yes":
        other_bidders = True
        clear_console()
    else:
        other_bidders = False
        highest_bid = 0
        for price in bids:
            if price > bids[price]:
                highest_bid = price
            
            
print(f"The winner is {bidder_name} with a bid of ${bid_price}.")

#print(bids)