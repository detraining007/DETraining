N=int(input("Enter the Number of Rows: "))
val=N-1
for row in range(N):
 for space in range(val-row):
   print(" ",end=" ")
 for col in range(2*row+1):
   print("*",end=" ")
 print()

