# PTR EXCEPTION
try:
	P = float(input('enter the principle :'))
	I = float(input('enter the simple interest : '))
	R = float(input('enter the rate of interest : '))
	T = I*100/P*R
	print(T)
except Exception as error:
	print(' P or R cannot be zero')
	if P==0 or R==0:
		raise Exception('Denominator cannot be zero')
finally:
	print('try again')

	
	