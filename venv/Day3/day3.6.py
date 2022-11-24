# ##Logical Operator
#
# ### Multiple statement with bill calculator
#
# print("Welcome to the Roller Coster")
# print("---------------"*2)
# height = int(input("Enter Your Highet in cm: "))
# bill= 0
# if height>=120:
#     print("You can Ride")
#     age = int(input("Enter your age: "))
#     if age<=12:
#         bill=5
#         print("Child Ticket is 5$")
#     elif age<=18:
#         bill = 7
#         print("Youth Tickets is 7$")
#     elif age>=45 and age<=55:
#         bill=0
#         print("Elder people price is 0$")
#     else:
#         bill=12
#         print("Adult tikcets is 12$")
#
#     photo=input("Do you want photo? Y or N:")
#     if photo=='Y':
#         if age>=45 and age<=55:
#             bill+=0
#         else:
#             bill+=3
#     print(f"Your total bill is ${bill}")
# else:
#     print("You can't ride")


#################Calculator using lower and count function

print("Welcome to the Calculator")

name1=input("Enter your name:\n")
name2=input("Enter your partner name:\n")

join_name=name1+name2
low_case_name=join_name.lower()

t = low_case_name.count("t")
l = low_case_name.count("l")
r = low_case_name.count("r")
o = low_case_name.count("o")
u = low_case_name.count("u")
v = low_case_name.count("v")
e = low_case_name.count("e")

tr=t+r+u+e
lv=e+o+v+l

total_num=str(tr)+str(lv)
total_num_count=int(total_num)

if total_num_count<10 or total_num_count>90:
    print(f"Your Total score is {total_num_count}, You go like mentos coke")

elif total_num_count>=40 and total_num_count<=50:
    print(f"Your Total score is {total_num_count}, You all great")

else:
    print(f"Your Total score is {total_num_count}")







