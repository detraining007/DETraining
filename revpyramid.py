def pyramid(n):
	for i in range(n,0,-1):
		print(' '*(n-i),end="")
		print('* '*((i)))
if __name__=="__main__":
	n = int(input("enter number of rows : "))
	py=pyramid(n)