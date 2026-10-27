n = int(input("Enter how many numbers: "))
largest = float(input("Enter a number: "))
for i in range(n - 1):
    num = float(input("Enter a number: "))
    if num > largest:
        largest = num
print(f"The largest number is {largest}")