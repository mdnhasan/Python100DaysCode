# tips calculator using number and math
# Number calculation
# F String

print("Welcome to the TIPS calculator")
print("---------------"*2)

total_bill = float(input("What is the total bill? $"))
tip_percentage = int(input("What percentage tip like to give? 10,12 or 15 %"))
total_people = int(input("How many people to split the bill?"))

tip_as_percentage= tip_percentage/100
total_tip_amount= tip_as_percentage*total_bill
total_bil_with_tips= total_bill+total_tip_amount
bill_per_person= total_bil_with_tips/total_people
final_amount=round(bill_per_person,2)

##Using math method
all_amount=((tip_percentage/100*total_bill+total_bill)/total_people)
final_amount2= round(all_amount,2)

print(f"Each Person will pay {final_amount}")##using F string
print("Each Person will pay: " + str(final_amount2)) ## using concat method and covert to str

###format with 2 decimal float
final_amount="{:.2f}".format(final_amount)
final_amount2="{:.2f}".format(final_amount2)

print(f"Each Person will pay with format {final_amount}")
print("Each Person will pay with format: " + str(final_amount2))

