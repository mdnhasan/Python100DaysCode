# ## pizza order code challenge
# ## Method 1 (My own)
#
# print("Welcome to Pizza Center")
# size= input("What size of Pizza you want? S,M or L: ")
# add_pepo =input("Do you want Extra Pepperoni? Y or N: ")
# extra_chesse = input("Do you want Extra Chesse? Y or N: ")
# bill=0
# pepo=0
# chesse=0
#
# if size=='S':
#     bill=15
#     pepo=2
#     chesse=1
#     newbill=0
#     print(f"Small Pizza: ${bill}")
#     if add_pepo=='Y' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for Medium or Large Pizza ${pepo}")
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='N' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='Y' and extra_chesse=='N':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo
#         print(f"Your final bill is ${newbill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# elif size=='M':
#     bill=20
#     pepo=3
#     chesse=1
#     newbill=0
#     print(f"Medium Pizza: ${bill}")
#     if add_pepo=='Y' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for Medium or Large Pizza ${pepo}")
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='N' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='Y' and extra_chesse=='N':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo
#         print(f"Your final bill is ${newbill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# elif size=='L':
#     bill=25
#     pepo=3
#     chesse=1
#     newbill=0
#     print(f"Large Pizza: ${bill}")
#     if add_pepo=='Y' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for Medium or Large Pizza ${pepo}")
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='N' and extra_chesse=='Y':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+chesse
#         print(f"Your final bill is ${newbill}")
#     elif add_pepo=='Y' and extra_chesse=='N':
#         print(f"Extra Pepperoni for all Pizza ${chesse}")
#         newbill=bill+pepo
#         print(f"Your final bill is ${newbill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# else:
#     print("Invalid Choice")


##Method 2 Guideline
print("Welcome to Pizza Center")
size= input("What size of Pizza you want? S,M or L: ")
add_pepo =input("Do you want Extra Pepperoni? Y or N: ")
extra_chesse = input("Do you want Extra Chesse? Y or N: ")
bill=0
pepo=0
chesse=0

if size=='S':
    bill+=15
    print(f"Small Pizza: ${bill}")

elif size=='M':
    bill+=20
    print(f"Medium Pizza: ${bill}")

elif size=='L':
    bill+=25
    print(f"Large Pizza: ${bill}")
else:
    print("Invalid Choiche")


if add_pepo=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
if extra_chesse=='Y':
    bill+=1
print(f"Your Final Bill: ${bill}")


