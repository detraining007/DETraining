def add_(n1,n2):
	return n1+n2
def sub_(n1,n2):
	return n1-n2
def mul_(n1,n2):
	return n1*n2
def div_(n1,n2):
	return n1//n2

if __name__=="__main__":
		n1=int(input("enter the  1st number: "))
		n2=int(input("enter the 2nd number: "))
		ch=int(input("enter choice from 1-4: "))
		if ch==1:
			sum=add_(n1,n2)
			print(" Sum is ", sum)
		elif ch==2:
			diff=sub_(n1,n2)
			print(" Difference is ", diff)
		elif ch==3:
			mul=mul_(n1,n2)
			print("Multiplication is ", mul)
		elif ch==4:
			div=div_(n1,n2)
			print(" Divison is ", div)
		else:
			print("Choice is not there")
			