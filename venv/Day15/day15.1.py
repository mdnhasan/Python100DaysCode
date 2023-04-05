from info import MENU,resources

profit=0

def is_resource_available(oder_ingredients):
    for item in oder_ingredients:
        if oder_ingredients[item]>=resources[item]:
            print(f"Sorry There is no enough{item}")
            return False
    return True


def make_coffe(drink_name, oder_ingredients):
    for item in oder_ingredients:
        resources[item]-=oder_ingredients[item]

def process_coin():
    """Retrun Total from inserted coin"""
    print("Please Insert Coin: ")
    total=int(input("How Many Quarters: ")) * 0.25
    total += int(input("How Many dimes: ")) * 0.1
    total += int(input("How Many nickels: ")) * 0.05
    total += int(input("How Many pennies: ")) * 0.01
    print(total)
    return total


def is_transaction_successful(money_received,cost_of_coffe):
    """Check enough money or not"""
    if money_received>cost_of_coffe:
        change=round(money_received-cost_of_coffe, 2)
        print(f"Here is ${change} change")
        global profit
        profit+=cost_of_coffe
        return True
    else:
        print("Sorry Need more money")
        return False


is_on =True
while is_on:
    user_choice = input("What do you want.(Espresso/Latte/Cappuccino): ").lower()
    if user_choice=='off':
        print("Machine now in maintenance Mode")
        is_on=False
    #elif user_choice=='espresso' or user_choice=='latte' or user_choice=='cappuccino':
        #is_on=True
    elif user_choice=='report': ######## Prepare Report
        print(f"Water: {resources['water']}ML")
        print(f"Milk: {resources['milk']}ML")
        print(f"Coffe: {resources['coffee']}ML")
        print(f"Money: ${profit} ")
        is_on=True
    else:
        drink=MENU[user_choice]
        if is_resource_available(drink['ingredients']):
            payment=process_coin()
            if is_transaction_successful(payment,drink['cost']):
                make_coffe(user_choice,drink['ingredients'])



