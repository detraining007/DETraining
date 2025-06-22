#Fibonnic element 

def fibbonnic(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonnic(n-1)+fibbonnic(n-2)
    

if __name__=="__main__":
    n = int(input("Enter the number of elements in the fibbonic series: "))
    print("Fibbonnic number is:",fibbonnic(n))