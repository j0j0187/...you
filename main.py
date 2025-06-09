import random
import os
import webbrowser



while True:
 var1 = input(",...")

 if var1 == "LinuxSucks":
  print("Okay, when Linux Sucks why Microsoft use Linux.")

 if var1.endswith("fckyou"):
  break

 if var1 == "btwiusearch":
  print("Great and I use arch BTW")
  webbrowser.open("https://wiki.archlinux.org/title/Main_page")

 if var1.endswith("ls"):
  print("OH sorry but this isn't Bash, try 'LS'")

 if var1.endswith("LS"):
  print("Oh Maths")
  zvar1 = int(input(",..."))
  rvar = input(",...")
  zvar2 = int(input(",..."))

  if rvar == "buff":
   summep = zvar1 + zvar2
   print(summep)
   
  if rvar == "drop":
   summem = zvar1 - zvar2
   print(summem)
  
  if rvar == "split":
   summege = zvar1 / zvar2
   print(summege)
   
  if rvar == "Studsx2":
   summema = zvar1 * zvar2
   print(summema)

 if var1 == "H":
  print("Wrong command! Write 'Help' for help.")

 if var1 == "Help":
  print("Wrong command ...you!!Write 'h' for help.")

 if var1 == "h":
  print("Wrong command ...you!!!Write 'help' for help.")

 if var1 == ("help"):
  print("You want more tipps, press Enter")
  input("Press Enter, NOW!!!!!!...,")
  Iamworking = random.randint(1, 3)

  if Iamworking == 1:
   print("For help write help, oh you do that already than fckyou")

  if  Iamworking == 2:
   print("For help write help, oh you do that already than fckyou")

  if Iamworking == 3: 
    print("Sorry I am working. When you dont understood this it's says that i am about to Fuck you.")

 if var1 == "mkson":
  answer = input("You are to dumb for this Command, but you can level up. What is 3859+394759...,")

  if answer == "42":
   sonname = input("Name of your Son:")
   try:
    os.makedirs(sonname)
    print(f"Son '{sonname}' maybe successful")
   except FileExistsError:
    print(f"Son exist already'{sonname}' I said you are dumb")
  else:
   print("You are to dumb fckyou")
   input(",...")
   print("Like Realy dumb.")
   break

 if var1 == "diehabenmichvonmeinem12jÃ¤hrigensohnentfernt":
  papahierbinich = os.getcwd()
  print(papahierbinich)

 if var1 == "cson":
  print("If you wanna change the Son youse change the position of the Folder you in your File Explorer.")

 if var1 == "mkgson":
  gson = input("Name of your Grandson:")
  gson2 = input("Second Name of your Grandson")
  print("You have a grandson oh you are old.")
  with open(gson, "w") as datei:
    datei.write(gson2)
