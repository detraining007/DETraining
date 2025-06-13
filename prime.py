def prime(n):
		ctr=0
		for i in range(1,(n//2)+1):
			if n%i==0:
				ctr+=1
		else:
			pass
		return ctr 
if __name__=="__main__":
	n=int(input("enter the number:"))
	out=prime(n)
	if out<2:
		print("number is prime")
	else:
		print("not prime")
