def Primenumber(num):
 count=0
 if(num<=1):
    return False
 elif num>1:
    for i in range(1,num+1):
       if num%i==0:
        count = count +1
    return count
if __name__ =="__main__":
   num=int(input("Enter the number: "))
   count=Primenumber(num)
   if count==2:
    print("Primenumber")
   else:
    print("not Primenumber")