studnets_score= input("Input all heights. Example: 123 134\n").split()
for n in range(0,len(studnets_score)): ###loop all number
    studnets_score[n]=int(studnets_score[n]) ###convert all number to INT
print(studnets_score)


maximum_score =0

for max in studnets_score:
    if max>maximum_score:
        maximum_score=max
print(f"The highest score is {maximum_score}")



