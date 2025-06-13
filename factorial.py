def factorial(n):
	result=n
	for i in range(n-1,0,-1):
		result=result*i
	return result
if __name__=="__main__":
	n=int(input("enter  numbers"))
	print(factorial(n))






