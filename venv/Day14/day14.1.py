from art import logo
from art import vs
from gamedata import data
import random


### Format the account Data using function
def format_data(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    account_follower_count=account["follower_count"]

    return (f"{account_name} a {account_description} from {account_country}")

##### Use If Else to check user guess



### Display Art

print(logo)

### Generate a random number from data
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)

print(f"Compare A: {format_data(account_a)}")
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

#guess=input("Who has more follower,'A' or 'B':  ").lower()

### check user guess right or wrong
##### Get Follower Account
account_a_follower=account_a["follower_count"]
account_b_follower=account_b["follower_count"]
print(account_a_follower)
print(account_b_follower)

##### Use If Else


### give user feedback based on their guess


### Score Keeping


### Make the game repetable until user did wrong


### making B to A for next


### Clear the screen between rounds





