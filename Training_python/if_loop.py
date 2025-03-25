# num = input("Enter ur no")
# num=int(num)
# if num%2==0:
#     print("no is even")
# else:
#     print("no is odd")


indian = ["pickle","panipuri","samosa"]
italian=["pizza","pasta","kichdi"]
chinese = ["fried rice","gobi","kebab"]

dish=input("Enter your dish")

if dish in indian:
    print("Indian dish")
elif dish in chinese:
    print("chinese dish")
elif dish in italian:
    print("italian dish")
else:
    print("I dont know which dish is ", dish)