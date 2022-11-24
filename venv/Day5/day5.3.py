

total_sum_even= 0

for i in range(0,101):
    if i%2 ==0:
        total_sum_even+=i
print(total_sum_even)


total_sum_odd= 0

for j in range(0,101):
    if j%2 !=0:
        total_sum_odd+=j
print(total_sum_odd)


total_sum= 0

for k in range(0,101,2): ##### 2 will add with each number example 0+2, 2+2,4+2
    total_sum+=k
print(total_sum)