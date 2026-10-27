rows = int(input("Enter number of rows: "))
for row_loop_var in range(1, rows + 1):
    for j in range(rows - row_loop_var):
        print(" ", end="") 
    for k in range(2 * row_loop_var - 1):
        print("*", end="")  
    print()