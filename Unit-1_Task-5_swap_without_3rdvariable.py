#Aim:python program to swap two numbers without using third variable.
a=int(input("ENTER THE FIRST NUM:"))
b=int(input("ENTER THE SECOND NUM:"))
print("before swapping:",a,b)
a=a+b
b=a-b
a=a-b
print("After swapping:",a,b)
