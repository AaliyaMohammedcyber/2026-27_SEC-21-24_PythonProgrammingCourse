#AIM:python program to calculate compound interest.
p=float(input('ENTER THE PRINCIPAL AMOUNT(IN ₹):'))
r=float(input('ENTER THE ANNUAL INTEREST RATE(IN %):'))
n=float(input('ENTER THE NO.OF TIMES INTEREST IS COMPOUNDED PER YEAR:'))
t=float(input('ENTER THE TIME(IN YEARS):'))
A=p*(1+r/n)**(n*t)
ci=A-p
print(' THE COMPOUND INTEREST IS:(IN ₹)',ci)