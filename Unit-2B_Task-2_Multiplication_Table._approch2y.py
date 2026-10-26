Num=int(input("ENTER A NUMBER FOR multiplication table:"))
mul=int(input("ENTER THE NUMBER OF FACTORS:"))
for factors in range(1,mul+1):
    print(f"{Num} x {factors} =",Num*factors)
else:
    print(f"THE MUTIPLICATIN TABLE OF {Num} upto {factors}!!")