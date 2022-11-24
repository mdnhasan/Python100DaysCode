# programming_dictionary =\
#     {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#      "Function": "A piece of code that you can easily call over and over again.",
#      123: "number"
#
#      }
# ######call data from dict..
# print(programming_dictionary[123])
#
#
# ####Adding item to dict
#
# programming_dictionary["Loop"]="circle"
#
# print(programming_dictionary)
#
# #######create empty Dict
#
# empty_dict={}
#
# #wipe all data from dict
# # programming_dictionary={}
# # print(programming_dictionary)
#
#
# ### edit dict
#
# # programming_dictionary["Bug"]="Error"
# # print(programming_dictionary)
#
# for things in programming_dictionary:
#     print(things) #####output key
#     print(programming_dictionary[things]) ###output key value




#########################Coding Challenge##########
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] >=90:
        student_grades[student]="Outstandings"
    elif student_scores[student] >=80:
        student_grades[student] = "Exceeds Expectation"
    elif student_scores[student] >70:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <=70:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

