'''
try:
    n1 =[1,2,3,4,5]
    print(n1[3])
except IndexError as msg:
    print(msg)
   

x=14
if not type(x) is str:
    raise Exception("only strings are allowed")

'''

for i in [1,2,3,4,5,6,7]:
    if i%2==0:
        print("even number", i)
        
