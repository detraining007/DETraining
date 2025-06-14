ord=int(input("enter the number"))
dig=int(input("enter the number"))
dig2=int(input("enter the number"))

listo=[(n1,n2,n3) for n1 in range(ord)  for n2 in range(dig)  for n3 in range(dig2) ]
print(listo)
