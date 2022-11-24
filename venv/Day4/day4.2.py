##########List in python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California",
                     "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

print(states_of_america[1])
print(states_of_america[-1])
print(states_of_america)
states_of_america[1]="My choice"
print(states_of_america)
states_of_america.append("My Other Choice")
print(states_of_america)
states_of_america.extend(["Dhaka","NGN"])
print(states_of_america)



# ######List Code challenege with banker roulete
# import random
#
# all_names=input("Enter all name: ")
# names=all_names.split(',')
# print(names)
# # names=['nasim', 'nirob', 'sam']##fixed list
# length=len(names)
#
# random_pep=random.randint(0, length-1)
#
# bill_person=names[random_pep]
# # bill_person=random.choice(names)---using choice
# print(f"{bill_person} will give the bill")
