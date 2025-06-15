Val=int(input("Enter the No.of Rows: "))
row=(Val//2)-1
col=2
print("*"*Val,end="\n")
while row!=0:
  while col<=(Val-2):
    print("*"*row,end="")
    print(" "*col,end="")
    print("*"*row)
    row=row-1
    col=col+2