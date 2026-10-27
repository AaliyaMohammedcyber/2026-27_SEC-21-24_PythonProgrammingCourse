# Print numbers in a 3 × 3 grid using while and for loops
num = 1
row = 1
while row <= 3:
    for col in range(1, 4):
        print(num, end=" ")
        num += 1
    print()
    row += 1