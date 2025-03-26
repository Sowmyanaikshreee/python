rows = 5
 
for i in range(rows):
    print(" " * i, end="")  
    for j in range(rows - i, 0, -1):
        print(j, end="")
    print()
 
 