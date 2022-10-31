# write a programme to calculate factorial of a given number using for loop 


# n! = 1 X 2 X 3 X 4 X .....X N-1 X N
#  5! = 1x2x3x4x5


from math import factorial


num=int(input("Enter your number: "))
factorial=1
for i in range (1,num+1):
    factorial = factorial * i
print(f"The  factorial of {num}  is {factorial} ")
    
    