#INVERSE OF STAR PATTERN
Val=int(input("Enter the Number of Rows: "))
for row in range(1,Val+1):
  for col in range(Val-row):
    print(" ",end=" ")
  for k in range(row):
    print("*",end=" ")
  print()

for row in range(Val-1,0,-1):
  for col in range(Val-row):
    print(" ",end=" ")
  for k in range(row):
    print("*",end=" ")
  print()