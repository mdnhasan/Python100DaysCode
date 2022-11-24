# ###### Nested if, elif statement
# print("Welcome to the Roller Coster")
# print("---------------"*2)
# height = int(input("Enter Your Highet in cm: "))
#
# if height>=120:
#     print("You can Ride")
#     age = int(input("Enter your age: "))
#     if age<=12:
#         print("Your Ticket price is 5$")
#     elif age<=18:
#         print("Your Ticket price is 7$")
#     else:
#         print("Your Ticket price is 12$")
# else:
#     print("You can't ride")


########## BMI Calculator with nested loop
height= float(input("Enter Height: "))
weigth = float(input("Enter Weight: "))

calculation =(weigth/(height ** 2))
BMI= round(calculation)
# BMI=21

if BMI<18.5:
    print(f"Your BMI is {BMI}, You are slightly underweight")
elif BMI<25:
    print(f"Your BMI is {BMI}, You are normal weight")
elif BMI<30:
    print(f"Your BMI is {BMI}, You are slightly overweight")
elif BMI<35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, You are clinicaly obese")