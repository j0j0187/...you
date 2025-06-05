import random
import os

while True:
 var1 = input("...,")
 if var1.endswith("fckyou"):
  break
 if var1.endswith("LS"):
  zvar1 = int(input("...,"))
  rvar = input("...,")
  zvar2 = int(input("...,"))
  if rvar == "buff":
   summep = zvar1 + zvar2
   print(summep)
   
  if rvar == "drop":
   summem = zvar1 - zvar2
   print(summem)
  
  if rvar == "split":
   summege = zvar1 / zvar2
   print(summege)
   
  if rvar == "*":
   summema = zvar1 * zvar2
   print(summema)
 if var1 == ("help"):
  print("You want more tipps, press Enter")
  input("Press Enter, NOW!!!!!!...,")
  Iamworking = random.randint(1, 3)
  if Iamworking == 1:
   print("For help write help, oh you do that alraedy than fckyou")
  if  Iamworking == 2:
   print("For help write help, oh you do that alraedy than fckyou")
  if Iamworking == 3: 
    print("Sorry I am working. When you dont understood this it's says that i am about to Fuck you.")
 if var1 == "mkson":
  answer = input("You are to dumb for this Command, but you can level up. What is 3859+394759...,")
  if answer == "idk":
   sonname = input("Name of your Son:")
   try:
    os.makedirs(sonname)
    print(f"Son '{sonname}' wurde vieleicht erstellt")
   except FileExistsError:
    print(f"Ordner '{sonname}' existiert bereits.")
  else:
   print("You are to dumb fckyou")
   input("...,")
   print("Like Realy dumb.")
   break
