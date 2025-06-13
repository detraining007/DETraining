def acending_order(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
if __name__=="__main__":
    arr=[22,65,11,2,5]
    acending_order(arr)
    print(arr)
