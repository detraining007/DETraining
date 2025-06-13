try:
     n1=[1,2,3,4,5]
     num=int(input("enter number:"))
     print(n1[num])
except IndexError as msg:
     print("enter :index"+str(num))






x="harika"
if not type(x) is string:
    raise Exception("only string are allowed")



for i in [1,2,3,4,5,6,7,8]:
    print("even number")
 
