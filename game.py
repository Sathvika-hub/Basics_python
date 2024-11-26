import dice

print("*"*10,"HILL CLIMB FALL","*"*10)
player_1 = input("enter the player_1 name:")
player_2 = input("enter the player_2 name:")
list_a = []
list_b = []
i=0
while(sum(list_a)!=10 and sum(list_b)!=10):
   if(i%2==0 and input("player_1 enter p to play:")=='p'):
      if(sum(list_a)<10):
         diceno = dice.diceroll()
         print("\nDice no.-->",diceno)
         list_a.append(diceno)
      else:
         list_a.clear()
      print("Step no.-->",sum(list_a))
      i +=1
   elif(i%2!=0 and input("player_1 enter p to play:")=='p'):
       if(sum(list_b)<10):
         diceno = dice.diceroll()
         print("\nDice no.-->",diceno)
         list_b.append(diceno)
       else:
         list_b.clear()
       print("Step no.-->",sum(list_b))
       i +=1    
   else:
      break

if(sum(list_a)==10):
   print("*"*10,f"{player_1} is the winner...","*"*10)
elif(sum(list_b)==10):
   print("*"*10,f"{player_2} is the winner...","*"*10)
else:
   print("Thankyou..")