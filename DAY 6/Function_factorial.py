num = int(input("Enter the number"))

def Factorial(num):
    sum = 1
    for i in range(num,0,-1):
        sum = sum*i
    print(sum)

Factorial(num)