n = 5

for i in range(n):

    # spaces
    for space in range(n - i - 1):
        print(" ", end=" ")

    num = 1

    # numbers
    for j in range(i + 1):
        print(num, end="   ")

        num = num * (i - j) // (j + 1)

    print()