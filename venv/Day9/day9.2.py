# ####### Nesting list in dict
#
# # travel_log ={
# #     "BD":["Dhaka", "RajShahi"],
# #     "IND":["Kolkata", "Mumbai"]
# # }
# # #print(travel_log)
# #
# # ##### Nesting dict in dict
# #
# # travel_log ={
# #     "BD":{"city_visited":["Dhaka", "RajShahi"], "Total_Visit":10},
# #     "IND":{"city_visited":["Kolkata", "Mumbai"], "Total_Visit":12}
# # }
#
# #print(travel_log)
#
# #####Nesting Dict in list
# travel_log =[
#  {
#     "Country":"BD",
#     "city_visited":["Dhaka", "RajShahi"],
#     "Total_Visit":10
#  },
# {
#     "Country":"IN",
#     "city_visited":["Kolkata", "Mumbai"],
#     "Total_Visit":12
# }
# ]
#
# print(travel_log)
#
# for i in travel_log:
#     print(travel_log[0])



##########Coding Challenge
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇



def add_new_country(Country,total_time,CIty):
    new_country = {}
    new_country["country"]=Country
    new_country["visits"]=total_time
    new_country["cities"]=CIty
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
