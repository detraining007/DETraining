def selection_sort(arr1):
    for iter in range(len(arr1)-1):
        min = arr1[iter]
        index = iter
        for value in range(iter+1,len(arr1)):
            if arr1[value]<min:
                min = arr1[value]
                index = value
        arr1[index] = arr1[iter]
        arr1[iter] = min
    return arr1





if  __name__ == "__main__":
    arr1 = list(map(int,input("Enter values with spaces: ").split()))
    print("Array before selection sort:")
    print(arr1)
    print("Array after selection sort:")
    print(selection_sort(arr1))
