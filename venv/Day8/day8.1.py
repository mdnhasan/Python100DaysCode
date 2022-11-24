#
# a= int(input("Enter Number: "))
#
# def greet():
#     if a==1:
#         print("Hello")
#     elif a==2:
#         print("Hi")
#     else:
#         print("Invalid")
#
# greet()


# def greet_with_name(name):   ######function with input
#     print(f"Hello {name}")    ####name= Parameter (name of data)
#     print(f"Hi {name}")       #### nasim= Argument (Actual Data)
#
# greet_with_name("nasim")



#
# def greet_with(name, location): ######function with more than 1 input
#     print(f"Hello {name}")
#     print(f"Address {location}")
#
# # greet_with("nasim", "Dhaka")##positional Argument
# # greet_with("dhaka", "nasim")
#
# greet_with(location="Dhaka", name="Nasim") ##Keywordbase Argument



#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    total_can= math.ceil((height*width)/cover)
    print(f"You'll need {total_can} can")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

























