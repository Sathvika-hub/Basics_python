print("*"*20,"ATM Machine","*"*20)
amount=int(input("enter the amount"))
l = [500,200,100,50,20,10,5,2,1]
c = 0
cs = 0
for i in l:
    Notes = amount//i
    c = c + Notes
    print(f"{i} notes -->{Notes}")
    amount = amount%i           #amount = amount - i * Notes    
print("Minimum number of Notes:",c)    
    