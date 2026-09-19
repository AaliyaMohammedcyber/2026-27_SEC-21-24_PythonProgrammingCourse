#AIM:Operator Precedence and Operator Associativity.
a=int(input("ENTER A POSITIVE NUM:"))
b=int(input("ENTER A POSITIVE NUM:"))
#division precedence
print(f"The result of {a} / {b} is {a/b}")
print(f"The result of {a} // {b} is {a//b}")
#parethesis
result1=(a+b)*3
print(f"The result of ({a} + {b})*3 is {result1}")
#ASSOCIATIVITY PROPERTIES
#Multiplication and floor division
result2=a*b//2
print(f"The result of {a}*{b}//2 is {result2}")
#floor division
result3=a//10//2
print(f"The result of {a}//10//2 is {result3}")
#multiplication and exponent
result4=a+b*2**2
print(f"The result of {a}+{b}*2**2 is {result4}")
#parenthesis and mutiplication
result5=(a+b)*2
print(f"The result of ({a}+{b})*2 is {result5}")
#addition , multiplication and greater than 
result6=a+b*2 > 10
print(f"The result of {a}+{b}*2 > 10 is {result6}")
# Multiple operators (and , or)
result7=a > b and b > 1 or a < 0
print(f"The result of {a}>{b} and {b}> 1 or {a}< 0 is {result7}")





