def chunking(n,r):
    base=n//r
    left=n%r
    chunks=[]
    if r>n:
        chunks=[1]*n 
    else:
         for i in range(r):   
            if i<left:
                chunks.append(base+1)
            else:
                chunks.append(base)
    print("records in each bag:",chunks)
if __name__=="__main__":
    n=int(input("enter records:"))
    r=int(input("enter bags:"))
    chunking(n,r)
            

    
