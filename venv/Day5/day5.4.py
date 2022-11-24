###FizzBuzz challenge
### print 1 to 100 numbers
### if number%3=0 then say fizz
### if number%3=5 then say buzz
### if number%3=0 then say fizzbuzz
### all should come in 1 line
###Thoght from own>> Print how many numbers of fizz, buzz, fizzbuzz
### Thought from own >> ALso with inputted number by user

total_fizz=0
total_buzz=0
total_fizzbuzz=0

to_check=int(input("To which number you want to check:\n "))

for i in range(1,to_check+1):

    if i%3 ==0 and i%5!=0:
        total_fizz+=1
        i="Fizz"

    elif i%3 !=0 and i%5==0:
        total_buzz+=1
        i="Buzz"

    elif i%3 ==0 and i%5==0:
        total_fizzbuzz+=1
        i="FizzBuzz"


    print(i)

print(f"Total Fizz in 1 to {to_check} = {total_fizz}")
print(f"Total Buzz in 1 to {to_check} = {total_buzz}")
print(f"Total Fizz Buzz in 1 to {to_check} = {total_fizzbuzz}")



