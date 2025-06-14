def pyramid(n):
	for i in range(n):
		print(' '*(n-i),end="")
		print(' *'*((i+1)))
if __name__=="__main__":
	n = int(input("enter number of rows : "))
	py=pyramid(n)