N=int(input("Enter the Number of Rows: "))
val=N-1
# Full Diamond Pattern
#Firts Half
for row in range(N-1):
 for space in range(val-row):
   print(" ",end=" ")
 for col in range(2*row+1):
   print("*",end=" ")
 print()
#Second Half
for row in range(N-1,-1,-1):
 for space in range(val-row):
   print(" ",end=" ")
 for col in range(2*row+1):
   print("*",end=" ")
 print()


