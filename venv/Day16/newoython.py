
def even_cal(list):
    even_sum=0
    for i in list:
        if i%2==0:
            even_sum+=i
    return even_sum
list = [2, 4, 5, 6, 7, 8,100]
even_sum=even_cal(list)
print(even_sum)