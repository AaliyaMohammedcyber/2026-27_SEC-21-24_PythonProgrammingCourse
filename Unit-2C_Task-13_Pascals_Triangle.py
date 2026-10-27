rows = int(input("Enter number of rows: "))
for i in range(rows):
    num = 1
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i + 1):
        print(num, end=" ")
        num = num * (i - k) // (k + 1)
    print()