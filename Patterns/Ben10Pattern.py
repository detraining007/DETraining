#Sand Glass star pattern
Val=int(input("Enter the no.of Rows: "))
for row in range(Val-1,-1,-1):
  print(" "*(Val-row),end=" ")
  for col in range(row+1):
    print("*",end=" ")
  print()
for row in range(1,Val):
  print(" "*(Val-row),end=" ")
  for col in range(row+1):
    print("*",end=" ")
  print()