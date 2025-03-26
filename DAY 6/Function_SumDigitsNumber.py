num = int(input("Entee the number"))

def SumNumber(num):
    s=0
    while(num>0):
        rem = num%10
        s = s+rem
        num = num//10
    print(s)

SumNumber(num)








# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10  # Extract the last digit and add to total
#         n //= 10  # Remove the last digit
#     return total