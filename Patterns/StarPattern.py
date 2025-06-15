# Display Star Pattern
Val=int(input("Enter the Number of Rows: "))
for row in range(Val-1):
  for col in range(row+1):
    print("*",end=" ")
  print()

for row in range(Val-1,-1,-1):
  for col in range(row+1):
    print("*",end=" ")
  print()