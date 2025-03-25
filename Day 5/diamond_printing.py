# n = 5

# n2 = (n+3)//2                      # half length +1 e.g. 4 for n=5
# s = ''.join(map(str,range(1, n2))) # generate '123' for n=5

# for i in range(n):
#     stop = n//2-abs(i-n//2)        # calculate length of half-string 0,1,2,1,0 for n=5
#     S = s[:stop+1]                 # slice string
#     print(S.rjust(n2)+S[-2::-1])   # print line e.g. '123' + '21'

rows = 3

for i in range(1,rows+1):
    print(" "*(rows-i), end="")

    for j in range(1,i+1):
        print(j, end="")
    
    for j in range(i-1,0,-1):
        print(j,end="")

    print() 

for i in range(rows-1,0,-1):
    print(" "*(rows-i), end="")

    for j in range(1,i+1):
        print(j, end="")
    
    for j in range(i-1,0,-1):
        print(j,end="") 
        
    print()