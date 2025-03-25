# s = input("Enter a string :")
# s1 = ""

# for i in s:
#     s1 = i+s1
# print(s1)

# if(s1==s):
#     print('palindrome')
# else:
#     print("not palindrome")


s = input("enter a string: ")

if s==(s[::-1]):
    print("palindrome")
else:
    print("no")