def countVowel(s):
    Count=0
    for i in s:
        if i in "aeiouAEIOU":
            Count=Count+1
    print(Count)

s = input("enter the string")
countVowel(s)