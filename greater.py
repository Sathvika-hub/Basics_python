name=input()
marks=int(input())
if(marks>=90):
    grade="A"
elif(80<=marks<=89):
   grade="B"
elif(70<=marks<=79):
   grade="C"
elif(60<=marks<=69):
   grade="D"
elif(50<=marks<=60):
   grade="F"
print(grade)