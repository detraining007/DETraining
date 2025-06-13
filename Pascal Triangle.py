N=10
for row in range(N):
  print(" "*(N-row),end=" ")
  num=1
  for col in range(row+1):
    print(num,end=" ")
    num=num*(row-col)//(col+1)
  print()
