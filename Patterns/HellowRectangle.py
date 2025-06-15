#Hellow Rectangle

Val=10
spaces=Val-2
for row in range(Val):
  if row==0 or row==Val-1:
    print("* "*Val)
  else:
    print("* "+"  "*spaces+ "*")