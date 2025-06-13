def Prime_Number(num):
	count=1
	for div in range(1,num):
		if num%div==0:
			count=count+1
			
	if count>2:
		return False
		
	return True
	
if __name__=="__main__":
	num=int(input("enter a number"))
	prime=Prime_Number(num)
	if  prime==True:
		print("it's prime")
	else:
		print("it's not a prime")
