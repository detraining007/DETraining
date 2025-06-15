#Reverse Right-angled triangle

Val=int(input())
for row in range(Val-1,-1,-1):
  for col in range(0,row):
    print("*",end=" ")
  print()