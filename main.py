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
