a=int(input("Enter the 1st num:"))
b=int(input("Enter the 2nd num:"))
c=int(input("Enter the 3rd num:"))
if a >= 0 or b <= 0 or c >= 0:
    if a < b and a < c:
        print(f"The value of {a} is lessthan {b ,c}")
    if b < a and b < c:
        print(f"The value of {b} is lessthan {a ,c}")
    if c < b and c < a :
         print(f"The value of {c} is lessthan {a,b}")
