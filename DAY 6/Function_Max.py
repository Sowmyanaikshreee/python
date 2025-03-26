num1 = int(input("Enter n1"))
num2 = int(input("Enter n2"))
num3 = int(input("Enter n3"))

def Max(num1,num2,num3):
    if (num1>=num2 and num1>=num3):
        print(num1)
    elif(num2>=num1 and num2>=num3):
        print(num2)
    else:
        print(num3)   

Max(num1,num2,num3)    
