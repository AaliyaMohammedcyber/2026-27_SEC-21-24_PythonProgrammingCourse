a=int(input("Enter 1stnum ="))
b=int(input("Enter 2ndnum ="))
c=int(input("Enter 3rdnum ="))
if a>b or a>c:
    if a>c :
        print(f"{a} is greater than {c}")
    elif c>a or b<c:
        print(f"{c} is greater than {a},{b}")
elif b>a :
    print(f"{b} is greater than {a}")