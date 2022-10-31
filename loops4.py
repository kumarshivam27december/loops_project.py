# write a program to find whether a given numberr is prime or not 

'''num=int(input("Enter  your number please: "))

for x in range(1,):
    if x.endswith(1,3,5,7,9):
        print("your number is",x)         '''


num=int(input("Enter the number: "))
for i in range(2,num):
    if(num%i == 0):
        print("your given number is prime")
    else:
        print("your given no is even")



