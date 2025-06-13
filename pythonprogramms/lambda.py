# fun =  lambda x: x +10
# print(fun(10))

fun = [lambda x,i=i: x + i for i in range(10)]  # Capture i as default argument
results = [f(5) for f in fun]  # Call each lambda with argument 5
print(results)
