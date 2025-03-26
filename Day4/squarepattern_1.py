# rows =5

# for i in range(0,rows):
#     for j in range(0,rows):

#         if((i==0) or (j==0) or(i==rows-1) or (j==rows-1)or(j==2)&(i==2) ):
#             print("1",end=" ")
        
    
#         else:
#             print("0",end=" ")
        
#     print()

size = int(input("Enter an odd number for the pattern size: "))

if size % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or (i == size // 2 and j == size // 2):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
