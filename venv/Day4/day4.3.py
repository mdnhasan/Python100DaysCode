# ###index with nested list
##### list in list
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
#                      "Georgia", "Connecticut", "Massachusetts",
#                      "Maryland", "South Carolina", "New Hampshire",
#                      "Virginia", "New York", "North Carolina",
#                      "Rhode Island", "Vermont", "Kentucky",
#                      "Tennessee", "Ohio", "Louisiana", "Indiana",
#                      "Mississippi", "Illinois", "Alabama", "Maine",
#                      "Missouri", "Arkansas", "Michigan", "Florida",
#                      "Texas", "Iowa", "Wisconsin", "California",
#                      "Minnesota", "Oregon", "Kansas", "West Virginia",
#                      "Nevada", "Nebraska", "Colorado", "North Dakota",
#                      "South Dakota", "Montana", "Washington", "Idaho",
#                      "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
#                      "Alaska", "Hawaii"]
#
# total_num=len(states_of_america)
# print(states_of_america[total_num-1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale",
#                "Nectarines", "Apples", "Grapes", "Peaches",
#                "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


# fruits=["Strawberries", "Spinach", "Kale","Nectarines", "Apples"]
# vege=["Grapes", "Peaches","Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen=[fruits, vege] ###### two list in single list
# print(dirty_dozen[0])
# print(dirty_dozen[1])
#
# print(dirty_dozen[0][0])
# print(dirty_dozen[1][1])
##############Code Challenge using index list

row1=[" 🥲 "," 🥲 "," 🥲 "," 🥲 "]
row2=[" 🥲 "," 🥲 "," 🥲 "," 🥲 "]
row3=[" 🥲 "," 🥲 "," 🥲 "," 🥲 "]
row4=[" 🥲 "," 🥲 "," 🥲 "," 🥲 "]

map= [row1,row2,row3,row4]
print(f"{row1}\n{row2}\n{row3}\n{row4}")

position= input("which position do you input: ")


horizontal=int(position[0])
vertical=int(position[1])
# print(map[vertical-1])

# selected_row=map[vertical-1]
# selected_row[horizontal-1]='X'
map[vertical-1][horizontal-1]='X'

print(f"{row1}\n{row2}\n{row3}\n{row4}")


