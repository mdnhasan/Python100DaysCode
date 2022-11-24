######for loop

# fruit_list=["Apple", "Orange", "Peach"]
# for fruit in fruit_list:
#     print(fruit)


########### Code Challenge
student_heights= input("Input all heights. Example: 123 134\n").split() ### Takes input and makes list using split


for n in range(0,len(student_heights)): ## set n=0 and count all from 0 to splitted number
    student_heights[n]=int(student_heights[n]) ## create all number INT
print(student_heights)

total_height=0
for height in student_heights:
    total_height+=height ### start from 0 takes every input and sum one by one
print(total_height)


number_of_studnet=0
for number in student_heights:
    number_of_studnet+=1 #start from 0 takes every input and sum one+1 and then one+1+1
print(number_of_studnet)

avarage_student_height=round(total_height/number_of_studnet)

print(avarage_student_height)