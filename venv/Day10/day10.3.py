from art import logo
print(logo)
#
# ##Addition
# def addtion(n1, n2):
#     """Add number"""
#     return n1+n2
# ##Subtraction
# def subtraction(n1, n2):
#     """Sub number"""
#     return n1-n2
#
# ##Multiplication
# def multiplication(n1, n2):
#     """Multiply number"""
#     return n1*n2
#
# ##Divison
# def divison(n1, n2):
#     """Divided number"""
#     return n1/n2
#
# operations={"+":addtion,"-":subtraction,"*":multiplication,"/":divison}
#
# num1= int(input("Enter first Number: "))
#
# for symbol in operations:
#     print(symbol)
#
# operation_symbol= (input("Pick any operation symbol: "))
# num2= int(input("Enter second Number: "))
#
# calculation_function=operations[operation_symbol]
# first_answer = calculation_function(num1, num2)
#
# print(f"{num1} {operation_symbol} {num2}= {first_answer}")
#
#
#
# operation_symbol= (input("Pick another operation symbol: "))
# num3= int(input("Enter another Number: "))
# calculation_function=operations[operation_symbol]
#
# second_answer = calculation_function(first_answer,num3)
#
# print(f"{first_answer} {operation_symbol} {num3}= {second_answer}")



# ###########Using While Loop
#
# ##Addition
# def addtion(n1, n2):
#     """Add number"""
#     return n1 + n2
#
#
# ##Subtraction
# def subtraction(n1, n2):
#     """Sub number"""
#     return n1 - n2
#
#
# ##Multiplication
# def multiplication(n1, n2):
#     """Multiply number"""
#     return n1 * n2
#
#
# ##Divison
# def divison(n1, n2):
#     """Divided number"""
#     return n1 / n2
#
#
# operations = {"+": addtion, "-": subtraction, "*": multiplication, "/": divison}
#
# num1 = int(input("Enter first Number: "))
#
# for symbol in operations:
#     print(symbol)
#
# should_continue =True
#
# while should_continue:
#
#     operation_symbol = (input("Pick any operation symbol: "))
#     num2 = int(input("Enter another Number: "))
#
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#
#     print(f"{num1} {operation_symbol} {num2}= {answer}")
#     user_choice= input(f"Type Y to calculating with {answer} or N to exit ").lower()
#     if user_choice=="y":
#         num1=answer
#     else:
#         should_continue=False





###############Recursion

###########Using While Loop

##Addition
def addtion(n1, n2):
    """Add number"""
    return n1 + n2


##Subtraction
def subtraction(n1, n2):
    """Sub number"""
    return n1 - n2


##Multiplication
def multiplication(n1, n2):
    """Multiply number"""
    return n1 * n2


##Divison
def divison(n1, n2):
    """Divided number"""
    return n1 / n2


operations = {"+": addtion, "-": subtraction, "*": multiplication, "/": divison}

def calculator():
    """Calculator using recursive function to call again with new start from fresh and continue while loop"""

    num1 = float(input("Enter first Number: "))

    for symbol in operations:
        print(symbol)

    should_continue =True

    while should_continue:

        operation_symbol = (input("Pick any operation symbol: "))
        num2 = float(input("Enter another Number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2}= {answer}")
        user_choice= input(f"Type Y to calculating with {answer} or N to exit ").lower()
        if user_choice=="y":
            num1=answer
        elif user_choice=="n":
            should_continue=False
        else:
            should_continue=False
            calculator() ######### this will again call calculator function from fresh start
calculator ### function called








