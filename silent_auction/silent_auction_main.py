import os

from silent_auction_art import logo
print(logo)

bids = {}
other_bidders = True

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while other_bidders:
    
    bidder_name = input("What is your name?\n")
    bid_price = int(input("What is your bid?\n$"))
    bids[bidder_name] = bid_price
    
    are_there_other_bidders = (input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if are_there_other_bidders == "yes":
        other_bidders = True
        clear_console()
    else:
        other_bidders = False
        highest_bidder(bids)
             