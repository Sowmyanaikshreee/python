rows = 3

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j % 2, end="")

    for j in range(i - 1, 0, -1):
        print(j % 2, end="")

    print()

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j % 2, end="")

    for j in range(i - 1, 0, -1):
        print(j % 2, end="")

    print()
