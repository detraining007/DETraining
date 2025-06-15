#StarTriangle
Val=int(input("Enter the no.of Rows: "))
for row in range(Val):
  print(" "*(Val-row),end=" ")
  for col in range(0,row):
    print("*",end="")
  print()
