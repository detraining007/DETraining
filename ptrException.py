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

	
'''
Output:

enter the principle : 0
enter the simple interest : 567
enter the rate of interest : 54
 P or R cannot be zero
try again

    T = I*100/P*R
        ~~~~~^~
ZeroDivisionError: float division by zero

During handling of the above exception, another exception occurred:

    raise Exception('Denominator cannot be zero')
Exception: Denominator cannot be zero

'''