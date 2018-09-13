inputvalid = False

while inputvalid == False:
   name = input("Hey Person, what's your name? ")
   if all(x.isalpha() or x.isspace() for x in name):
     inputvalid = True
   else:
     inputvalid = False
 
print(name)
