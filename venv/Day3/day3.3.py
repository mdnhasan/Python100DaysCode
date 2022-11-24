### Leaf Year Code Challenge

year = int(input("Enter Year to check:"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This is a Leaf Year")
        else:
            print("This is not a Leaf Year")
    else:
        print("This is a leaf year")
else:
    print("This is not a leaf year")