from art import logo
from art import vs
from gamedata import data
import random


### Format the account Data using function
def format_data(account):  ######create a list account from Dictnary "Data" and took info
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]

    return (f"{account_name} a {account_description} from {account_country}") ## show data from dict with format

##### Use If Else to check user guess

def check_answer(guess,a_follower,b_follower): ## user answer compare with a & b follower number
    if a_follower>b_follower:
        return guess=='a'
    else:
        return guess=='b'

### Display Art

print(logo)
score=0
game_should_continue=True
account_b=random.choice(data) ####### Account B will be actual random generation

### Make the game repetable until user did wrong

while game_should_continue: ### while loop here because all other in loop data
    ### Generate a random number from data
    account_a=account_b ### account b random string set into Account A when loop through
    account_b=random.choice(data) ## again generate B to compare date
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}") ## call function and param account
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # ### Format the account Data
    # account_name=account_a["name"]
    # account_description=account_a["description"]
    # account_country=account_a["country"]
    #
    #
    #
    # print(f"{account_name} a {account_description} from {account_country}")

    ### User Guess

    guess=input("Who has more follower,'A' or 'B':  ").lower()

    ### check user guess right or wrong
    ##### Get Follower Account
    account_a_follower=account_a["follower_count"] ## count all the follower from dict
    account_b_follower=account_b["follower_count"]
    #print(account_a_follower)
    #print(account_b_follower)

    is_correct=check_answer(guess,account_a_follower,account_b_follower)

    ### give user feedback based on their guess
    ### Score Keeping
    if is_correct:
        score+=1
        print(f"You are Right, Your score is {score}")
    else:
        print(f"Sorry you lost. The final score {score}")
        game_should_continue=False

### making B to A for next


### Clear the screen between rounds





