from art import logo
#from replit import clear
print(logo)
print("Welcome to Bid App")


bid={}
bid_finished = False

def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bids in bidding_record:
        price=bidding_record[bids]
        if price>highest_bid:
            highest_bid=price
            winner=bids
    print(f"The winner is {winner} with amount {highest_bid}")



while not bid_finished:
    name=input("Enter Name: ")
    bid_amount=int(input("BiD amount: "))
    bid[name]=bid_amount
    more_bid=input("Are any bidder. Yes or No: ").lower()
    if more_bid=="no":
        bid_finished=True
        highest_bidder(bidding_record=bid)







