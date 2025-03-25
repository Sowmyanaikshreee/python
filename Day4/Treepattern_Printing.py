# rows = 4

# for i in range(rows):
#     print(" "*(rows-i-1),end="")
#     print("*" * (2*i+1))

n = 3  # Number of rows

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == i:
            print("1", end="")
        else:
            print("0", end="")
    print()
