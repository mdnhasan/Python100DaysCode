### Multiple statement with bill calculator

print("Welcome to the Roller Coster")
print("---------------"*2)
height = int(input("Enter Your Highet in cm: "))
bill= 0
if height>=120:
    print("You can Ride")
    age = int(input("Enter your age: "))
    if age<=12:
        bill=5
        print("Child Ticket is 5$")
    elif age<=18:
        bill = 7
        print("Youth Tickets is 7$")
    else:
        bill=12
        print("Adult tikcets is 12$")

    photo=input("Do you want photo? Y or N:")
    if photo=='Y':
        bill+=3
    print(f"Your total bill is {bill}")
else:
    print("You can't ride")
