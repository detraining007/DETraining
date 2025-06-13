def selection(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
if __name__=="__main__":
    arr=[32,4,15,100,74,2]
    selection(arr)
    print(arr)
    