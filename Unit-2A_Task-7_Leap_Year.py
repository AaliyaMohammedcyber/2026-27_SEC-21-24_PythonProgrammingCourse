year = int(input("Enter the year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(f"The given year ({year}) is a leap year")
    else:
        print(f"The given year ({year}) is not a leap year")
else:
    if year % 4 == 0:
        print(f"The given year ({year}) is a leap year")
    else:
        print(f"The given year ({year}) is not a leap year")    