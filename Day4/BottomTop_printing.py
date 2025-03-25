# rows = 5

# for i in range(0, rows):
#     for j in range(0,i+1):
#         print("1",end="")
#     print("\r")

# rows = 6

# for i in range(1,rows):
#     for j in range(i):
#         print(i, end='')
#     print('')

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")

