#AIM:Write a python program to check whether a number is positive, negative, or zero.
num=int(input("ENTER A NUMBER:"))
if num > 0:
    print(F"{num} is a POSITIVE NUMBER")
elif num < 0:
    print(f"{num} is a NEGATIVE NUMBER")
else:
    print("ZERO")