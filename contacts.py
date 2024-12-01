contact = ["Sathvika","Madhumitha","Soumya","Sahithi","Srilekha","Shirisha","Poojitha","Chandana","Ashwitha","Sathvika","Anusha"]
while True:
 search = input("Enter contact:").capitalize()
 for i in contact:
  if i.startswith(search):
   print(i)
