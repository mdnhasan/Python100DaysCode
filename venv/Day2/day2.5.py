# How many days live challenge

age = int(input("Enter Age: "))

livedDays= age*365
livedWeeks= age*52
livedMonths=age*12

lifelengthdays= 90*365
lifelengthweeks = 90*52
lifelengthmonths= 90*12

remaindays = int(lifelengthdays) - int(livedDays)
remainweeks= int(lifelengthweeks) - int(livedWeeks)
remainmonths = int(lifelengthmonths) - int(livedMonths)

print(f" You have {remaindays} days, {remainweeks} weeks and {remainmonths} months left")
