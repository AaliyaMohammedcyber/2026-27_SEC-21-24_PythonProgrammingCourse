#Logical operator
#And operator
a=5
result=a>2 and a<5
answer=a>2 and a<10
print("output of",a,">2 and <5 is:",result)
print("output of",a,">2 and <10 is:",answer)
#Or operator
result1=a<2 or a<5
answer1=a>2 or a<10
print("output of",a,">2 or <5 is:",result1)
print("output of",a,"<2 or <10 is:",answer1)
#Not operator
result2=not(a>2 and a<5)
answer2=not(a>2 and a<10)
print("output of",a,">2 not <5 is:",result2)
print("output of",a,">2 not <10 is:",answer2)