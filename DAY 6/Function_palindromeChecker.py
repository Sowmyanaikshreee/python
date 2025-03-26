pal = input("Enter the string")

def Palindrome(pal):
    if pal==pal[::-1]:
        print("string is palindrome")
    else:
        print("string is not plaindrome")

Palindrome(pal)