def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n



if __name__=="__main__":
    try:
        x=factorial(998)
        print(x)
    except RecursionError:
        print("Error") 
   
    
