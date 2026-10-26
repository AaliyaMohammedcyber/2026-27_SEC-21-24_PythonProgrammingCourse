a=float(input("ENTER THE FIRST SIDE(IN M):"))
b=float(input("ENTER THE SECOND SIDE(IN M):"))
c=float(input("ENTER THE THIRD SIDE(IN M):"))
if a + b > c and b + c > a and a + c > a :
    print("IT IS A TRIANGLE")
else:
    print("IT'S NOT A TRIANGLE")